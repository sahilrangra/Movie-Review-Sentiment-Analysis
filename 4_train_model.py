from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

# Load dataset & embeddings
df = pd.read_csv("movie_reviews_100.csv")
embeddings = np.load("movie_embeddings_100.npy")

# Train regression model
X_train = embeddings
y_train = df["sentiment"].values

regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Save model
import pickle
with open("regression_model.pkl", "wb") as f:
    pickle.dump(regressor, f)

print("✅ Regression model trained and saved!")
