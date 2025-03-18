# **Movie Review Sentiment Analysis (RAG + ML Model)**

## **📌 Project Overview**
This project is a **hybrid sentiment analysis system** that combines:
1. **Retrieval-Augmented Generation (RAG)** using FAISS to find similar movie reviews.
2. **Machine Learning Regression Model** to predict sentiment scores based on embeddings.
3. **Sentence Embeddings** from `all-MiniLM-L6-v2` for numerical representation.

It allows users to enter a movie review and get **two sentiment scores**:
- **RAG Score** (based on similar reviews from dataset)
- **Regression Model Score** (ML-predicted sentiment)

---
## **🚀 Features**
✅ **100 movie reviews dataset** (balanced positive, neutral, and negative)
✅ **Retrieves similar reviews using FAISS**
✅ **Predicts sentiment score using ML regression**
✅ **Supports user input for real-time sentiment analysis**
✅ **Easily expandable with more reviews & models**

---
## **🛠️ Installation & Setup**
### **1️⃣ Install Dependencies**
```bash
pip install numpy pandas faiss-cpu sentence-transformers scikit-learn
```

### **2️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/movie-sentiment-analysis.git
cd movie-sentiment-analysis
```

### **3️⃣ Run Each Step in Order**
```bash
python dataset.py       # Create and save the dataset
python embeddings.py    # Generate embeddings
python faiss_store.py   # Store embeddings in FAISS
python train_model.py   # Train regression model
python predict.py       # Test with your own review
```

---
## **📝 Usage**
Run `predict.py` and enter a movie review:
```bash
python predict.py
```
Example Input:
```bash
Enter your movie review: This movie was absolutely fantastic!
```
Example Output:
```
🔍 RAG-Based Sentiment Score: 0.95
📊 Regression Model Prediction: 0.92
```

---
## **📂 Project Structure**
```
📦 movie-sentiment-analysis
├── dataset.py         # Creates & saves movie_reviews_100.csv
├── embeddings.py      # Converts reviews to embeddings
├── faiss_store.py     # Stores embeddings in FAISS index
├── train_model.py     # Trains regression model
├── predict.py         # User input & sentiment prediction
├── movie_reviews_100.csv  # Dataset file
├── movie_embeddings_100.npy  # Saved embeddings
├── movie_index_100.faiss  # FAISS index
├── regression_model.pkl  # Trained regression model
└── README.md          # Project documentation
```

---
## **📌 Future Improvements**
🔹 Expand dataset to 1000+ reviews for better accuracy.
🔹 Fine-tune a Transformer model for better predictions.
🔹 Integrate a Flask API for a web-based interface.
🔹 Improve slang & explicit word detection.

---
## **🤝 Contributing**
Feel free to **fork**, **open issues**, or **submit pull requests**!

📧 **Contact:** [sahilsinghrangra96@gmail.com]

⭐ **If you found this useful, give it a star on GitHub!** ⭐

