from google_play_scraper import Sort, reviews
import pandas as pd
from datetime import datetime, timedelta
import os

def scrape_play_store_reviews(app_id="com.spotify.music", max_reviews=2000):
    print(f"Scraping Play Store reviews for {app_id}...")
    
    result, continuation_token = reviews(
        app_id,
        lang='en', # defaults to 'en'
        country='us', # defaults to 'us'
        sort=Sort.NEWEST, # defaults to Sort.NEWEST
        count=max_reviews # defaults to 100
    )
    
    # Filter for the last 12 months
    one_year_ago = datetime.now() - timedelta(days=365)
    filtered_reviews = [r for r in result if r['at'] >= one_year_ago]
    
    print(f"Collected {len(filtered_reviews)} reviews from the last 12 months.")
    
    df = pd.DataFrame(filtered_reviews)
    if not df.empty:
        # Normalize the schema
        df = df[['reviewId', 'content', 'score', 'at']]
        df.columns = ['id', 'text', 'rating', 'date']
        df['source'] = 'Google Play Store'
        
        os.makedirs('data', exist_ok=True)
        df.to_csv('data/play_store_reviews.csv', index=False)
        print("Saved to data/play_store_reviews.csv")
    return df

if __name__ == "__main__":
    scrape_play_store_reviews()
