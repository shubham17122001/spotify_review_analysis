import google.generativeai as genai
import os

class ChatEngine:
    def __init__(self):
        # Assumes API key is configured elsewhere (in main.py)
        # We use flash for faster chat responses
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        self.chat = self.model.start_chat(history=[])
        
    def get_response(self, query, context_df):
        """Answers a user query based on the context dataset."""
        # Convert context to string, taking a sample if it's too large for flash 
        # (flash has 1M context too, but better to be safe)
        sample_df = context_df.sample(min(len(context_df), 1000)) 
        context_str = sample_df.to_csv(index=False)
        
        prompt = f"""
        You are an AI assistant inside the 'Ask the Reviews' feature of a Product Management dashboard.
        Your job is to answer questions about user feedback for Spotify.
        Base your answers strictly on the following review data:
        
        {context_str}
        
        User Question: {query}
        """
        
        try:
            response = self.chat.send_message(prompt)
            return response.text
        except Exception as e:
            return f"Error communicating with AI: {e}"
