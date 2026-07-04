import sys
import os
# Add parent directory to sys.path to resolve 'app' imports correctly when running in Streamlit Cloud
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from app.discovery_engine import DiscoveryEngine

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)

# Premium Custom Styling for Spotify Dark Theme
st.set_page_config(page_title="Spotify AI-Native Discovery Co-Pilot", layout="wide")

st.markdown("""
<style>
    /* Dark theme overrides and card styling */
    .stApp {
        background-color: #121212;
        color: #FFFFFF;
    }
    h1, h2, h3 {
        color: #FFFFFF !important;
        font-family: 'Outfit', 'Inter', sans-serif;
    }
    
    /* Custom Spotify Style Card */
    .track-card {
        background-color: #181818;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        border: 1px solid #282828;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    
    .track-card:hover {
        transform: translateY(-5px);
        border-color: #1DB954;
        box-shadow: 0 10px 20px rgba(29, 185, 84, 0.15);
    }
    
    .track-header {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 8px;
    }
    
    .track-title {
        font-size: 1.35rem;
        font-weight: 700;
        color: #FFFFFF;
        margin: 0;
    }
    
    .track-artist {
        font-size: 1.0rem;
        color: #B3B3B3;
        margin: 2px 0 10px 0;
    }
    
    .badge-container {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        margin-bottom: 12px;
    }
    
    .badge {
        font-size: 0.75rem;
        font-weight: 700;
        padding: 4px 10px;
        border-radius: 20px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .badge-indie {
        background-color: #1DB954;
        color: #121212;
    }
    
    .badge-major {
        background-color: #3E3E3E;
        color: #FFFFFF;
    }
    
    .badge-match {
        background-image: linear-gradient(135deg, #7928CA 0%, #FF0080 100%);
        color: #FFFFFF;
    }
    
    .badge-novelty {
        background-color: #0070F3;
        color: #FFFFFF;
    }
    
    .badge-familiar {
        background-color: #F5A623;
        color: #121212;
    }
    
    .ai-explanation {
        background-color: #242424;
        border-left: 4px solid #1DB954;
        border-radius: 4px;
        padding: 12px 16px;
        margin-top: 15px;
        font-style: italic;
        color: #E0E0E0;
        font-size: 0.95rem;
        line-height: 1.4;
    }
    
    .popularity-bar {
        background-color: #2A2A2A;
        border-radius: 10px;
        height: 6px;
        width: 100%;
        margin-top: 6px;
        overflow: hidden;
    }
    
    .popularity-fill {
        background-color: #B3B3B3;
        height: 100%;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🎧 Spotify AI-Native Discovery Co-Pilot")
st.markdown("Escape your recommendation bubbles! Describe your exact vibe, control the novelty factor, and discover new independent artists.")

st.markdown("""
**How this AI-Native MVP differs from traditional recommendations:**
*   **Dynamic Discovery Intensity:** Puts you in control of the familiarity/novelty ratio.
*   **Niche Boost:** Actively bypasses major label commercial placement loops to surface independent talent.
*   **Semantic Reasoning:** Translates text descriptions of a mood into sonic selections, explaining its choices transparently.
""")

col_ctrl, col_results = st.columns([1, 2])

with col_ctrl:
    st.subheader("Discovery Tuning Panel")
    
    # Select predefined persona to quickly configure parameters
    persona = st.selectbox(
        "Load Research Persona Configuration",
        options=["Manual Configuration", "Elena (Indie Supporter)", "Priya (Daily Mix Stagnation)", "Marcus (Genre Specialist)"]
    )
    
    # Set default values based on persona
    default_vibe = "moody late night driving music with synths"
    default_intensity = 50
    default_niche = False
    
    if persona == "Elena (Indie Supporter)":
        default_vibe = "melancholic indie guitar tracks by local artists"
        default_intensity = 80
        default_niche = True
    elif persona == "Priya (Daily Mix Stagnation)":
        default_vibe = "relaxing study beats to focus without lyrics"
        default_intensity = 60
        default_niche = False
    elif persona == "Marcus (Genre Specialist)":
        default_vibe = "deep ambient space synth or avant-garde jazz"
        default_intensity = 95
        default_niche = True
        
    vibe_input = st.text_area(
        "Describe the vibe, instruments, or mood you want to discover:",
        value=default_vibe,
        height=100,
        help="Example: 'Breezy acoustic roadtrip vibes with smooth vocals' or 'spooky retro synths for gaming'"
    )
    
    discovery_intensity = st.slider(
        "Discovery Intensity (Novelty vs Familiarity)",
        min_value=0,
        max_value=100,
        value=default_intensity,
        help="0% plays only familiar/major hits. 100% pushes deep into obscure/independent catalogs."
    )
    
    niche_boost = st.toggle(
        "Niche Boost (Prioritize Independent Labels)",
        value=default_niche,
        help="Boosts independent labels and filters out major commercial catalog tracks."
    )
    
    generate_btn = st.button("Generate Discovery Queue", type="primary")

with col_results:
    st.subheader("Your Custom Discovery Queue")
    
    if generate_btn:
        with st.spinner("AI Co-Pilot is reasoning over catalog coordinates..."):
            engine = DiscoveryEngine()
            results = engine.generate_discovery_queue(vibe_input, discovery_intensity, niche_boost)
            
            if not results:
                st.info("No tracks matched your specific criteria. Try easing the sliders or expanding your vibe prompt.")
            else:
                for item in results:
                    track = item["track"]
                    score = item["match_score"]
                    is_novel = item["is_novel"]
                    rationale = item["ai_rationale"]
                    
                    # Set custom label tags
                    label_badge = f'<span class="badge badge-indie">Independent</span>' if track["label_type"] == "Independent" else f'<span class="badge badge-major">Major Label</span>'
                    novel_badge = f'<span class="badge badge-novelty">Discovery</span>' if is_novel else f'<span class="badge badge-familiar">Familiar Hit</span>'
                    
                    track_html = f"""
                    <div class="track-card">
                        <div class="track-header">
                            <div>
                                <div class="track-title">{track["title"]}</div>
                                <div class="track-artist">{track["artist"]} &nbsp;|&nbsp; <span style="color:#B3B3B3; font-size:0.9rem;">{track["genre"]}</span></div>
                            </div>
                            <div style="text-align: right;">
                                <span class="badge badge-match">{score}% Match</span>
                            </div>
                        </div>
                        <div class="badge-container">
                            {label_badge}
                            {novel_badge}
                        </div>
                        <div style="font-size:0.85rem; color:#B3B3B3; margin-bottom: 2px;">Popularity Index: {track["popularity"]}/100</div>
                        <div class="popularity-bar">
                            <div class="popularity-fill" style="width: {track["popularity"]}%;"></div>
                        </div>
                        <div class="ai-explanation">
                            💡 <b>AI Co-Pilot Rationale:</b> {rationale}
                        </div>
                    </div>
                    """
                    st.markdown(track_html, unsafe_allow_html=True)
    else:
        st.info("Adjust the parameters in the left panel and click 'Generate Discovery Queue' to run the AI Co-Pilot.")
