import faiss
import numpy as np
import pandas as pd
import pickle
from sentence_transformers import SentenceTransformer

# Load all necessary components
df = pd.read_csv("movie_reviews_100.csv")
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
index = faiss.read_index("movie_index_100.faiss")

# Load trained regression model
with open("regression_model.pkl", "rb") as f:
    regressor = pickle.load(f)

def predict_sentiment(query, top_k=3):
    query_embedding = model.encode([query], convert_to_numpy=True)

    # Retrieve similar reviews
    distances, indices = index.search(query_embedding, top_k)
    similar_reviews = df.iloc[indices[0]]
    avg_sentiment = similar_reviews["sentiment"].mean()

    # Predict using regression model
    predicted_sentiment = regressor.predict(query_embedding)[0]

    return avg_sentiment, predicted_sentiment

# Ask user for input
query = input("Enter your movie review: ")

# Predict sentiment
avg_sentiment, pred_sentiment = predict_sentiment(query)

print("\n🔍 RAG-Based Sentiment Score:", round(avg_sentiment, 2))
print("📊 Regression Model Prediction:", round(pred_sentiment, 2))

