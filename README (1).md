# Sentiment Analysis on Google Play Store Reviews (Tokopedia App)

This project is a sentiment analysis pipeline using user reviews scraped from the Tokopedia app on Google Play Store. The project includes data scraping, preprocessing, feature extraction, model training, and evaluation.

## 📂 Project Structure

```
submission-3/
├── dataset/
│   └── reviews_scraped.csv
├── scraper.py
├── sentiment_analysis_notebook.ipynb
├── requirements.txt
├── README.md
```

## 📝 Project Overview

- **Data Source**: Google Play Store reviews of Tokopedia app (scraped using `google-play-scraper`)
- **Language**: Indonesian
- **Task**: Classify user reviews into 3 sentiment categories: positive, neutral, and negative.

## 🔄 Workflow

1. **Scraping**: Collected >3,000 user reviews from Google Play Store using Python.
2. **Preprocessing**:
   - Case folding
   - Removing special characters & URLs
   - Stopwords removal (Indonesian stopwords)
   - Stemming using Sastrawi
3. **Feature Extraction**: TF-IDF Vectorizer (unigram & bigram)
4. **Model Training**:
   - Logistic Regression
   - Naive Bayes (to be added)
   - Support Vector Machine (to be added)
5. **Evaluation**:
   - Accuracy
   - Confusion Matrix
   - Classification Report (Precision, Recall, F1-Score)

## 🚀 How to Run

1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/sentiment-analysis-tokopedia.git
   cd sentiment-analysis-tokopedia
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Scrape the data**:
   ```bash
   python scraper.py
   ```

4. **Open notebook**:
   - Run `sentiment_analysis_notebook.ipynb` to train and evaluate the model.

## 🛠️ Dependencies

- pandas
- numpy
- nltk
- Sastrawi
- scikit-learn
- seaborn
- matplotlib
- google-play-scraper

## 📊 Results

- Achieved accuracy of **>85%** on test data with Logistic Regression.
- Further experiments with Naive Bayes and SVM will be added.

## 📌 Notes

- Dataset is saved under `dataset/reviews_scraped.csv`
- This project is part of a sentiment analysis submission challenge.

## 📄 License

This project is licensed under the MIT License.
