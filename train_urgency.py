import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

# Load dataset
data = pd.read_csv("data/tickets.csv")

# Input and target
X = data["ticket"]
y = data["urgency"]

# Create ML pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression(max_iter=1000))
])

# Train model
model.fit(X, y)

# Save trained model
joblib.dump(model, "models/urgency_model.pkl")

print("Urgency model trained successfully!")
print("Urgency levels:", sorted(y.unique().tolist()))
print("Model saved to: models/urgency_model.pkl")