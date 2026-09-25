import joblib

# Load trained models
category_model = joblib.load("models/category_model.pkl")
urgency_model = joblib.load("models/urgency_model.pkl")


# Confidence threshold
CONFIDENCE_THRESHOLD = 70


def review_ticket(ticket):
    # Predict category
    category = category_model.predict([ticket])[0]
    category_probabilities = category_model.predict_proba([ticket])[0]
    category_confidence = max(category_probabilities) * 100

    # Predict urgency
    urgency = urgency_model.predict([ticket])[0]
    urgency_probabilities = urgency_model.predict_proba([ticket])[0]
    urgency_confidence = max(urgency_probabilities) * 100

    # Human review decision
    if (
        category_confidence < CONFIDENCE_THRESHOLD
        or urgency_confidence < CONFIDENCE_THRESHOLD
    ):
        decision = "Human Review Required"
    else:
        decision = "Auto Route"

    return (
        category,
        urgency,
        category_confidence,
        urgency_confidence,
        decision
    )


# Test ticket
ticket = "My payment was charged twice"

result = review_ticket(ticket)

print("Ticket:", ticket)
print()
print("Category:", result[0])
print("Category Confidence:", round(result[2], 2), "%")
print()
print("Urgency:", result[1])
print("Urgency Confidence:", round(result[3], 2), "%")
print()
print("Decision:", result[4])