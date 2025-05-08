from dotenv import load_dotenv
import os
from openai import OpenAI
from openai.types.shared_params import APIStatusError

# Load API key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Instantiate OpenAI client
client = OpenAI(api_key="7g2v7do6VyF92G6GbCpN9NMSv5DSMW8ubCFjufudt1T08kcr4pTvJQQJ99BEACYeBjFXJ3w3AAABACOGItiC")

# Check API key validity by calling a valid method
try:
    models = client.models.list()
    print("✅ API key is valid. Available models:")
    for model in models.data[:5]:
        print("•", model.id)
except Exception as e:
    print(f"❌ Error: {e}")
