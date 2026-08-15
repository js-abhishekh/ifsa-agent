import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

key = os.getenv("OPENROUTER_API_KEY")
model = "nvidia/nemotron-3-ultra-550b-a55b:free"
base_url = "https://openrouter.ai/api/v1"

print(f"[test_openrouter] Calling OpenRouter model: {model}...")

llm = ChatOpenAI(
    model=model,
    api_key=key,
    base_url=base_url,
    temperature=0
)

res = llm.invoke([
    {"role": "system", "content": "You are a regulatory parameter extraction assistant. Output strict JSON only without markdown formatting."},
    {"role": "user", "content": "Extract: Tenor 5Y has a risk weight of 1.1% (0.011). Return JSON: {\"5Y\": 0.011}"}
])

print("\n[test_openrouter] Response from Nemotron Ultra:")
print(res.content)
