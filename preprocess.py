import pandas as pd
import re

# Load dataset
data = pd.read_csv("data/tickets.csv")


# Text preprocessing function
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


# Apply preprocessing
data["clean_ticket"] = data["ticket"].apply(clean_text)


# Display results
print("Text preprocessing completed successfully!")
print()
print(data[["ticket", "clean_ticket"]].head())