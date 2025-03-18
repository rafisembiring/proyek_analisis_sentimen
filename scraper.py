from google_play_scraper import reviews, Sort
import pandas as pd
import os

app_id = 'com.tokopedia.tkpd'  # Ganti ID sesuai aplikasi target kamu

def scrape_reviews(app_id, n=3000):
    result, _ = reviews(
        app_id,
        lang='id',  # Bahasa Indonesia
        country='id',
        sort=Sort.NEWEST,
        count=n,
    )

    df = pd.DataFrame(result)
    df = df[['userName', 'content', 'score']]
    df.columns = ['user', 'review', 'rating']
    df.dropna(inplace=True)
    return df

if __name__ == "__main__":
    df = scrape_reviews(app_id, n=4000)

    # Bikin folder kalau belum ada
    if not os.path.exists('dataset'):
        os.makedirs('dataset')

    df.to_csv('dataset/reviews_scraped.csv', index=False)
    print("Scraping selesai. Data disimpan di dataset/reviews_scraped.csv")
