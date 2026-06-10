from services.llm_service import LLMService

print("Start...")

llm = LLMService()

print("Client created")

response = llm.generate(
    "Say hello in one sentence."
)

print("Response:")
print(repr(response))