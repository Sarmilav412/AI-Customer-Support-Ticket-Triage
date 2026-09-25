import joblib

# Load trained models
category_model = joblib.load("models/category_model.pkl")
urgency_model = joblib.load("models/urgency_model.pkl")


def predict_ticket(ticket):
    # Predict category
    category = category_model.predict([ticket])[0]

    # Predict urgency
    urgency = urgency_model.predict([ticket])[0]

    # Get confidence scores
    category_probabilities = category_model.predict_proba([ticket])[0]
    urgency_probabilities = urgency_model.predict_proba([ticket])[0]

    category_confidence = max(category_probabilities) * 100
    urgency_confidence = max(urgency_probabilities) * 100

    return category, urgency, category_confidence, urgency_confidence


# Test ticket
ticket = "My payment was charged twice"

category, urgency, category_confidence, urgency_confidence = predict_ticket(ticket)

print("Ticket:", ticket)
print()
print("Predicted Category:", category)
print("Category Confidence:", round(category_confidence, 2), "%")
print()
print("Predicted Urgency:", urgency)
print("Urgency Confidence:", round(urgency_confidence, 2), "%")