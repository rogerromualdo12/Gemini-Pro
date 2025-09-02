from google import genai
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain what is an Annunaki, and who is Ra, no generes(solo recopila)"
)
print(response.text)