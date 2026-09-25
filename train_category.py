import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

# Load dataset
data = pd.read_csv("data/tickets.csv")

# Input and target
X = data["ticket"]
y = data["category"]

# Create ML pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression(max_iter=1000))
])

# Train model
model.fit(X, y)

# Save trained model
joblib.dump(model, "models/category_model.pkl")

print("Category model trained successfully!")
print("Categories:", sorted(y.unique().tolist()))
print("Model saved to: models/category_model.pkl")