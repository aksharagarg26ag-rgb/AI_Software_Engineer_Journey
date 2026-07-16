import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")


if api_key is None:
    print("API key not found!")
else:
    print("API key loaded successfully.")

print("API Key:")
print(api_key)