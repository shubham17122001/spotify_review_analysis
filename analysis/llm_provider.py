import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configure the API key
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables. Please check your .env file.")
genai.configure(api_key=API_KEY)

# Use Gemini 2.5 Flash for analysis
# We'll use gemini-2.5-flash as it is widely available
model = genai.GenerativeModel('gemini-2.5-flash')

def generate_insights(prompt, text_chunk):
    """Generates insights from a chunk of text using Gemini."""
    try:
        response = model.generate_content(f"{prompt}\n\nReviews Data:\n{text_chunk}")
        return response.text
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return ""
