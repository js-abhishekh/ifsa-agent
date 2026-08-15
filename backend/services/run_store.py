import asyncio
from typing import Dict, Any, Optional

class RunStore:
    def __init__(self):
        self._store: Dict[str, Dict[str, Any]] = {}
        self._queues: Dict[str, asyncio.Queue] = {}

    def create_run(self, run_id: str) -> None:
        if run_id not in self._store:
            self._store[run_id] = {}
        if run_id not in self._queues:
            self._queues[run_id] = asyncio.Queue()

    def set_state(self, run_id: str, state_slice: Dict[str, Any]) -> None:
        if run_id in self._store:
            self._store[run_id].update(state_slice)

    def get_state(self, run_id: str) -> Optional[Dict[str, Any]]:
        return self._store.get(run_id)

    def get_event_queue(self, run_id: str) -> Optional[asyncio.Queue]:
        return self._queues.get(run_id)

    async def push_event(self, run_id: str, event_dict: Dict[str, Any]) -> None:
        queue = self.get_event_queue(run_id)
        if queue:
            await queue.put(event_dict)

    async def mark_done(self, run_id: str) -> None:
        queue = self.get_event_queue(run_id)
        if queue:
            await queue.put(None)

run_store = RunStore()
