from typing import List, Dict, Any, Optional
from datetime import datetime
from src.graph.build_graph import build_frtb_graph
from src.graph.state import PortfolioPosition
from backend.services.run_store import run_store

app = build_frtb_graph()

def _serialize_state(state: Any) -> Any:
    if hasattr(state, "model_dump"):
        return state.model_dump()
    if isinstance(state, list):
        return [_serialize_state(item) for item in state]
    if isinstance(state, dict):
        return {k: _serialize_state(v) for k, v in state.items()}
    return state

async def run_pipeline(run_id: str, positions: List[Dict[str, Any]], pdf_path: Optional[str], max_retries: int):
    try:
        parsed_positions = [PortfolioPosition(**p) for p in positions]
        initial_state = {
            "user_query": "Compute FRTB-SA capital charges for the attached portfolio",
            "portfolio_inputs": parsed_positions,
            "document_path": pdf_path,
            "max_retries": max_retries,
            "retry_count": 0,
            "validation_errors": [],
            "audit_flags": [],
        }
        run_store.set_state(run_id, _serialize_state(initial_state))
        
        async for chunk in app.astream(initial_state, stream_mode="updates"):
            for node_name, node_state in chunk.items():
                event_data = {}
                node_state = _serialize_state(node_state)
                
                if node_name == "audit_document":
                    event_data = {"audit_flags": node_state.get("audit_flags", [])}
                elif node_name == "retrieve":
                    event_data = {"retrieved_count": len(node_state.get("retrieved_regulatory_nodes", []))}
                elif node_name == "extract_logic":
                    logic = node_state.get("extracted_calculation_logic", [])
                    event_data = {
                        "extracted_count": len(logic),
                        "is_complete": all(l.get("is_complete") for l in logic) if logic else False
                    }
                elif node_name == "execute_quant":
                    event_data = {"metrics": node_state.get("calculated_metrics", [])}
                elif node_name == "validate":
                    errors = node_state.get("validation_errors", [])
                    event_data = {
                        "validation_errors": len([e for e in errors if e.get("severity") == "blocking"]),
                        "warnings": len([e for e in errors if e.get("severity") == "warning"])
                    }
                else:
                    event_data = node_state

                event = {
                    "event": "node_complete",
                    "node": node_name,
                    "timestamp": datetime.utcnow().isoformat(),
                    "data": event_data
                }
                
                # Update store (merge with existing state instead of replacing)
                current_state = run_store.get_state(run_id) or {}
                # Update current state with new keys from node_state
                merged_state = {**current_state, **node_state}
                run_store.set_state(run_id, merged_state)
                
                # Push event
                await run_store.push_event(run_id, event)

        # Final state — emit flat structure for frontend hook
        final_state = run_store.get_state(run_id) or {}
        summary = final_state.get("final_compliance_summary")
        if not summary:
            summary = "Pipeline completed without blocking errors."
            
        await run_store.push_event(run_id, {
            "event": "done",
            "timestamp": datetime.utcnow().isoformat(),
            "final_compliance_summary": summary,
            "calculated_metrics": final_state.get("calculated_metrics", []),
            "audit_flags": final_state.get("audit_flags", []),
            "validation_errors": final_state.get("validation_errors", []),
            "portfolio_inputs": _serialize_state(final_state.get("portfolio_inputs", [])),
        })

    except Exception as e:
        await run_store.push_event(run_id, {
            "event": "error_event",  # matches frontend EventSource listener name
            "message": str(e),
            "timestamp": datetime.utcnow().isoformat()
        })
    finally:
        await run_store.mark_done(run_id)
