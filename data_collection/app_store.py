from app_store_scraper import AppStore
import pandas as pd
from datetime import datetime, timedelta
import os

def scrape_app_store_reviews(app_name="spotify-new-music-and-podcasts", app_id=324684580, max_reviews=2000):
    print(f"Scraping App Store reviews for {app_name}...")
    
    spotify = AppStore(country="us", app_name=app_name, app_id=app_id)
    spotify.review(how_many=max_reviews)
    
    reviews = spotify.reviews
    
    # Filter for the last 12 months
    one_year_ago = datetime.now() - timedelta(days=365)
    filtered_reviews = [r for r in reviews if r['date'] >= one_year_ago]
    
    # Limit to max_reviews if it exceeded
    filtered_reviews = filtered_reviews[:max_reviews]
    
    print(f"Collected {len(filtered_reviews)} reviews from the last 12 months.")
    
    df = pd.DataFrame(filtered_reviews)
    if not df.empty:
        # Normalize the schema to match Play Store
        # 'review' is the content in app-store-scraper
        df = df[['userName', 'review', 'rating', 'date']]
        df.columns = ['id', 'text', 'rating', 'date']
        df['source'] = 'Apple App Store'
        
        os.makedirs('data', exist_ok=True)
        df.to_csv('data/app_store_reviews.csv', index=False)
        print("Saved to data/app_store_reviews.csv")
    return df

if __name__ == "__main__":
    scrape_app_store_reviews()
