import joblib

# Load trained category model
category_model = joblib.load("models/category_model.pkl")


# Team mapping
team_mapping = {
    "Billing": "Billing Support Team",
    "Account": "Account Support Team",
    "Technical": "Technical Support Team",
    "Product": "Product Support Team"
}


def assign_team(ticket):
    # Predict category
    category = category_model.predict([ticket])[0]

    # Assign team
    team = team_mapping.get(category, "General Support Team")

    return category, team


# Test ticket
ticket = "My payment was charged twice"

category, team = assign_team(ticket)

print("Ticket:", ticket)
print()
print("Predicted Category:", category)
print("Assigned Team:", team)