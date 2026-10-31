import os
from dotenv import load_dotenv

load_dotenv()

required_keys = ("MISTRAL_API_KEY", "GROQ_API_KEY", "TAVILY_API_KEY")
missing_keys = [key for key in required_keys if not os.getenv(key, "").strip()]

if missing_keys:
    print("Missing required .env keys: " + ", ".join(missing_keys))
    raise SystemExit(1)

print("Mistral, Groq, and Tavily keys are configured (values withheld).")