import pandas as pd
import os

def normalize_data():
    print("Normalizing data from all sources...")
    
    dfs = []
    
    if os.path.exists('data/play_store_reviews.csv'):
        play_df = pd.read_csv('data/play_store_reviews.csv')
        dfs.append(play_df)
        
    if os.path.exists('data/app_store_reviews.csv'):
        app_df = pd.read_csv('data/app_store_reviews.csv')
        dfs.append(app_df)
        
    if not dfs:
        print("No data found to normalize.")
        return
        
    combined_df = pd.concat(dfs, ignore_index=True)
    
    # Ensure standard types
    combined_df['date'] = pd.to_datetime(combined_df['date'])
    combined_df['text'] = combined_df['text'].astype(str)
    
    # Remove extremely short reviews (less than 10 characters) which don't provide much value for analysis
    combined_df = combined_df[combined_df['text'].str.len() > 10]
    
    combined_df.to_csv('data/normalized_reviews.csv', index=False)
    print(f"Normalized {len(combined_df)} total reviews. Saved to data/normalized_reviews.csv")
    
if __name__ == "__main__":
    normalize_data()
