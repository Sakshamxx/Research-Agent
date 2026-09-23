import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

print("HF token loaded:", bool(token))

client = InferenceClient(
    api_key=token
)

response = client.chat.completions.create(
    model="openai/gpt-oss-120b:groq",
    messages=[
        {
            "role": "user",
            "content": "Explain RAG in one simple sentence."
        }
    ],
)

print(response.choices[0].message.content)