import google.generativeai as genai
import json
import os
from app.catalog import TRACKS

class DiscoveryEngine:
    def __init__(self):
        # We use gemini-2.5-flash for fast reasoning and structured outputs
        self.model = genai.GenerativeModel('gemini-2.5-flash')

    def generate_discovery_queue(self, user_prompt, discovery_intensity, niche_boost):
        """
        Generates a personalized queue of recommended songs from the catalog 
        based on a natural language prompt, discovery intensity (0-100), and niche boost.
        """
        
        # Serialize the catalog to send to Gemini
        catalog_str = json.dumps(TRACKS, indent=2)
        
        prompt = f"""
        You are the Spotify AI-Native Discovery Co-Pilot.
        Your task is to select 5 to 7 songs from the provided catalog that best fit the user's discovery request.
        
        User Search Input (The "Vibe"): "{user_prompt}"
        Discovery Intensity Slider: {discovery_intensity}/100 
        (0 means user wants highly familiar/mainstream music. 100 means user wants highly obscure/experimental indie music. 50 is balanced.)
        
        Niche Boost Active: {niche_boost}
        (If True, you MUST prioritize "Independent" labels and penalize high-popularity "Major" label songs.)
        
        Music Catalog:
        {catalog_str}
        
        Instructions:
        1. Parse the user's "Vibe" text. Match it semantically against the track genres, vibes, and sonic descriptions.
        2. Filter and rank the tracks based on Niche Boost:
           - If Niche Boost is True, rank tracks with label_type = "Independent" and popularity < 65 significantly higher.
        3. Balance Novelty and Familiarity based on the Discovery Intensity:
           - If Discovery Intensity is low (e.g. < 40), include 2-3 higher popularity tracks (popularity > 85, Major label).
           - If Discovery Intensity is high (e.g. > 70), favor obscure independent tracks (popularity < 55, Independent label).
        4. For each recommended track, generate a custom, friendly, and transparent "ai_rationale" explaining *exactly* why it was selected. Mention specific sonic elements from the catalog (e.g., specific instruments, tempo, vocals) and how they fit the user's vibe and settings.
        5. Output ONLY a valid JSON array of objects. Do not include markdown code block syntax (like ```json).
        
        JSON Schema to return:
        [
          {{
            "track_id": <int: id of the track from catalog>,
            "match_score": <int: score from 0-100 indicating semantic match strength>,
            "is_novel": <bool: true if the track counts as a discovery/obscure, false if it is a familiar/mainstream track>,
            "ai_rationale": "<string: detailed, personalized explanation of why this song was recommended>"
          }}
        ]
        """
        
        try:
            # We configure generation to enforce a JSON response format
            response = self.model.generate_content(
                prompt,
                generation_config={"response_mime_type": "application/json"}
            )
            
            # Parse response
            results = json.loads(response.text.strip())
            
            # Map recommendation details back to the actual tracks from catalog
            enriched_queue = []
            for rec in results:
                track_id = rec.get("track_id")
                track_data = next((t for t in TRACKS if t["id"] == track_id), None)
                if track_data:
                    enriched_queue.append({
                        "track": track_data,
                        "match_score": rec.get("match_score", 80),
                        "is_novel": rec.get("is_novel", True),
                        "ai_rationale": rec.get("ai_rationale", "Matches your vibe request.")
                    })
            
            # Sort by match score descending
            enriched_queue.sort(key=lambda x: x["match_score"], reverse=True)
            return enriched_queue
            
        except Exception as e:
            print(f"Error in discovery queue generation: {e}")
            # Return empty or fallback
            return []
