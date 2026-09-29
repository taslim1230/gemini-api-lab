from google import genai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise SystemExit(
        "Missing GEMINI_API_KEY. Add it to your .env file."
    )

# Create Gemini client
client = genai.Client(api_key=api_key)

# Take prompt from user
user_prompt = input("Enter your prompt: ").strip()

if not user_prompt:
    raise SystemExit("Prompt cannot be empty.")

# Send prompt to Gemini
response = client.interactions.create(
    model="gemini-3.8-flash",
    input=user_prompt
)

# Print response
print("\nAI Response:")
print(response.output_text)