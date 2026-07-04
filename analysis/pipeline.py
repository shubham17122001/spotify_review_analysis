import pandas as pd
import json
import os
from analysis.llm_provider import generate_insights

def run_analysis():
    if not os.path.exists('data/normalized_reviews.csv'):
        print("No normalized data found. Please run scrapers first.")
        return
        
    df = pd.read_csv('data/normalized_reviews.csv')
    
    # We want to format the data to send to Gemini
    # Let's take a sample if the dataset is massive, but Gemini 1.5 Pro can handle a lot.
    # We'll just convert it to a CSV string.
    reviews_text = df.to_csv(index=False)
    
    prompt = """
    You are a Product Manager on the Growth Team at Spotify.
    Analyze the following user reviews from the App Store and Google Play Store over the last 12-24 months.
    
    The company has successfully acquired millions of users and built one of the world's most sophisticated recommendation systems. However, a significant percentage of listening still comes from repeat playlists, familiar artists, previously discovered tracks.
    One of your company's strategic goals is to increase meaningful music discovery and reduce repetitive listening behavior.

    Based on the provided reviews, please generate a comprehensive Markdown report that includes:
    1. Sentiment Trends (overall sentiment and changes over time if visible in data)
    2. Theme Clusters (what are the most common frustrations with recommendations? why do users struggle to discover new music?)
    3. JTBD (Jobs-to-be-Done) Insights (what listening behaviors are users trying to achieve?)
    4. Personas (which user segments experience different discovery challenges?)
    5. Causes of Repetitive Listening (what causes users to repeatedly listen to the same content?)
    6. Opportunity Ranking (list the top unmet needs and rank them as product opportunities to improve discovery)

    Output the report in valid Markdown format. Ensure you answer the core assignment questions.
    """
    
    print("Sending data to Gemini for analysis (this might take a minute)...")
    report = generate_insights(prompt, reviews_text)
    
    if report:
        os.makedirs('data', exist_ok=True)
        with open('data/analysis_report.md', 'w', encoding='utf-8') as f:
            f.write(report)
        print("Analysis complete! Report saved to data/analysis_report.md")
    else:
        print("Failed to generate report.")

if __name__ == "__main__":
    run_analysis()
