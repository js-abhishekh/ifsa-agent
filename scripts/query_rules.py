import sys
sys.path.insert(0, '.')
from src.ingestion.vector_store import RegulatoryStore

store = RegulatoryStore()

queries = [
    ('vega curvature options non-linear', 'MarketRisk'),
    ('curvature shock upward downward', 'MarketRisk')
]

print('--- Regulatory Search Results ---')
for q, r_class in queries:
    res = store.query(q, n_results=5)
    docs = res.get('documents', [[]])[0]
    metas = res.get('metadatas', [[]])[0]
    print(f'\nQuery: {q}')
    for d, m in zip(docs, metas):
        clause = m.get("clause_id")
        text = d[:200].replace('\n', ' ')
        print(f'[{clause}] {text}...')
