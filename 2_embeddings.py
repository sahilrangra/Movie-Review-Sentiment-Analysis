from sentence_transformers import SentenceTransformer
import numpy as np
import pandas as pd

# Load dataset
df = pd.read_csv("movie_reviews_100.csv")

# Load embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Convert reviews to embeddings
embeddings = model.encode(df["review"].tolist(), convert_to_numpy=True)

# Save embeddings
np.save("movie_embeddings_100.npy", embeddings)

print("✅ Embeddings saved as movie_embeddings_100.npy")