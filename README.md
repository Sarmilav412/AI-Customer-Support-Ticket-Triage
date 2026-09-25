# AI Customer Support Ticket Triage System

## Intelligent Ticket Classification, Prioritization and Support Team Routing

### 📌 Project Overview

The **AI Customer Support Ticket Triage System** is a Python-based application designed to analyze customer support tickets and assist support teams in handling them efficiently.

The system classifies customer tickets into predefined categories, determines their urgency level, assigns the appropriate support team, calculates confidence scores, and identifies tickets that require human review.

The application also provides AI explanations, ticket history, and an analytics dashboard through an interactive Streamlit interface.

---

## 🎯 Objectives

- Automatically classify customer support tickets.
- Identify the urgency level of each ticket.
- Route tickets to the appropriate support team.
- Provide confidence scores for predictions.
- Identify low-confidence tickets for human review.
- Explain ticket classification and urgency.
- Maintain a history of analyzed tickets.
- Provide basic ticket analytics.

---

## ✨ Key Features

### 1. Ticket Classification

The system classifies tickets into four categories:

- Billing
- Account
- Technical
- Product

### 2. Urgency Detection

Tickets are assigned one of three urgency levels:

- High
- Medium
- Low

### 3. Confidence Score

The application displays confidence percentages for category and urgency predictions.

### 4. Automatic Team Routing

| Category | Support Team |
|---|---|
| Billing | Billing Support Team |
| Account | Account Support Team |
| Technical | Technical Support Team |
| Product | Product Support Team |

### 5. Human Review

If the prediction confidence is below the **70% threshold**, the system marks the ticket as:

**Human Review Required**

Otherwise:

**Auto Route**

### 6. AI Explanation

The application provides a simple explanation for the predicted category and urgency.

### 7. Ticket History

The system maintains a session-based history of analyzed tickets.

It records:

- Ticket ID
- Customer
- Category
- Urgency
- Assigned Team
- Category Confidence
- Urgency Confidence
- Routing Decision

### 8. Analytics Dashboard

The dashboard displays:

- Total tickets
- Automatically routed tickets
- Human review tickets
- Tickets by category
- Tickets by urgency

---

## 🔄 System Workflow

```text
Customer
   ↓
Support Ticket
   ↓
Text Analysis
   ↓
Category Prediction
   ↓
Urgency Prediction
   ↓
Confidence Evaluation
   ↓
Team Assignment
   ↓
AI Explanation
   ↓
Auto Route / Human Review
   ↓
Ticket History
   ↓
Analytics Dashboard
```

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Joblib
- Streamlit
- Natural Language Processing (NLP)
- TF-IDF
- Logistic Regression
- Git
- GitHub
- Visual Studio Code

---

## 📂 Project Structure

```text
AI-Customer-Support-Ticket-Triage/
│
├── app/
│   ├── human_review.py
│   ├── predict.py
│   ├── preprocess.py
│   ├── streamlit_app.py
│   ├── team_routing.py
│   ├── train_category.py
│   └── train_urgency.py
│
├── data/
│   └── tickets.csv
│
├── models/
│   ├── category_model.pkl
│   └── urgency_model.pkl
│
├── README.md
└── requirements.txt
```

---

## 📊 Dataset

The project uses a labeled customer support ticket dataset containing **100 sample tickets**.

### Categories

- Billing
- Account
- Technical
- Product

### Urgency Levels

- High
- Medium
- Low

---

## 🧠 Machine Learning Approach

The project uses Natural Language Processing techniques to process customer support ticket text.

### Text Representation

**TF-IDF (Term Frequency-Inverse Document Frequency)** is used to convert text into numerical features.

### Classification Algorithm

**Logistic Regression** is used for classification.

Separate models are used for:

1. Ticket Category Prediction
2. Ticket Urgency Prediction

The trained models are stored using Joblib.

---

## 💻 Application Interface

The Streamlit application allows users to enter:

- Ticket ID
- Customer Name
- Customer Email
- Customer Issue

After clicking **Analyze Ticket**, the application displays:

- Predicted Category
- Predicted Urgency
- Assigned Support Team
- Category Confidence
- Urgency Confidence
- AI Explanation
- Routing Decision
- Ticket Information
- Ticket History
- Analytics Dashboard

---

## ▶️ How to Run the Project

### Step 1: Open the project folder

```bash
cd C:\Users\HP\Desktop\AI-Customer-Support-Ticket-Triage
```

### Step 2: Activate the virtual environment

```bash
venv2\Scripts\activate
```

### Step 3: Run the Streamlit application

```bash
streamlit run app\streamlit_app.py
```

### Step 4: Open the application

The Streamlit application will open in the browser.

---

## 🧪 Example

### Input

```text
My payment was charged twice and I need a refund.
```

### Output

```text
Category: Billing
Urgency: High
Assigned Team: Billing Support Team
```

The application also displays confidence scores, an AI explanation, and a routing decision.

---

## 👨‍💼 Human Review Mechanism

The system uses a confidence threshold of **70%**.

```text
Confidence ≥ 70%
        ↓
    Auto Route

Confidence < 70%
        ↓
Human Review Required
```

This allows uncertain tickets to be checked by a human.

---

## 📈 Benefits

- Reduces manual ticket classification effort.
- Helps prioritize customer issues.
- Supports faster ticket routing.
- Provides prediction transparency.
- Helps support teams monitor ticket patterns.
- Provides a simple user-friendly interface.

---

## ⚠️ Limitations

- The dataset contains a limited number of sample tickets.
- Prediction quality depends on the available training data.
- Ambiguous tickets may require human review.
- The project is currently a prototype and demonstration application.
- Ticket history is session-based and is not stored permanently in a database.

---

## 🚀 Future Scope

- Larger real-world customer support datasets.
- Advanced NLP and transformer-based models.
- Integration with real customer support platforms.
- Persistent database storage.
- Email and notification integration.
- Multilingual ticket classification.
- Advanced analytics and reporting.
- Continuous model retraining.

---

## 🎓 Project Information

**Project Type:** Academic AI & Machine Learning Project

**Domain:** Artificial Intelligence, Natural Language Processing and Customer Support Automation

---

## 👩‍💻 Developed By

**Sarmila V**

**Bachelor of Engineering – Computer Science and Engineering**

---

## 📄 License# AI Customer Support Ticket Triage System

## Intelligent Ticket Classification, Prioritization and Support Team Routing

### 📌 Project Overview

The **AI Customer Support Ticket Triage System** is a Python-based application designed to analyze customer support tickets and assist support teams in handling them efficiently.

The system classifies customer tickets into predefined categories, determines their urgency level, assigns the appropriate support team, calculates confidence scores, and identifies tickets that require human review.

The application also provides AI explanations, ticket history, and an analytics dashboard through an interactive Streamlit interface.

---

## 🎯 Objectives

- Automatically classify customer support tickets.
- Identify the urgency level of each ticket.
- Route tickets to the appropriate support team.
- Provide confidence scores for predictions.
- Identify low-confidence tickets for human review.
- Explain ticket classification and urgency.
- Maintain a history of analyzed tickets.
- Provide basic ticket analytics.

---

## ✨ Key Features

### 1. Ticket Classification

The system classifies tickets into four categories:

- Billing
- Account
- Technical
- Product

### 2. Urgency Detection

Tickets are assigned one of three urgency levels:

- High
- Medium
- Low

### 3. Confidence Score

The application displays confidence percentages for category and urgency predictions.

### 4. Automatic Team Routing

| Category | Support Team |
|---|---|
| Billing | Billing Support Team |
| Account | Account Support Team |
| Technical | Technical Support Team |
| Product | Product Support Team |

### 5. Human Review

If the prediction confidence is below the **70% threshold**, the system marks the ticket as:

**Human Review Required**

Otherwise:

**Auto Route**

### 6. AI Explanation

The application provides a simple explanation for the predicted category and urgency.

### 7. Ticket History

The system maintains a session-based history of analyzed tickets.

It records:

- Ticket ID
- Customer
- Category
- Urgency
- Assigned Team
- Category Confidence
- Urgency Confidence
- Routing Decision

### 8. Analytics Dashboard

The dashboard displays:

- Total tickets
- Automatically routed tickets
- Human review tickets
- Tickets by category
- Tickets by urgency

---

## 🔄 System Workflow

```text
Customer
   ↓
Support Ticket
   ↓
Text Analysis
   ↓
Category Prediction
   ↓
Urgency Prediction
   ↓
Confidence Evaluation
   ↓
Team Assignment
   ↓
AI Explanation
   ↓
Auto Route / Human Review
   ↓
Ticket History
   ↓
Analytics Dashboard
```

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Joblib
- Streamlit
- Natural Language Processing (NLP)
- TF-IDF
- Logistic Regression
- Git
- GitHub
- Visual Studio Code

---

## 📂 Project Structure

```text
AI-Customer-Support-Ticket-Triage/
│
├── app/
│   ├── human_review.py
│   ├── predict.py
│   ├── preprocess.py
│   ├── streamlit_app.py
│   ├── team_routing.py
│   ├── train_category.py
│   └── train_urgency.py
│
├── data/
│   └── tickets.csv
│
├── models/
│   ├── category_model.pkl
│   └── urgency_model.pkl
│
├── README.md
└── requirements.txt
```

---

## 📊 Dataset

The project uses a labeled customer support ticket dataset containing **100 sample tickets**.

### Categories

- Billing
- Account
- Technical
- Product

### Urgency Levels

- High
- Medium
- Low

---

## 🧠 Machine Learning Approach

The project uses Natural Language Processing techniques to process customer support ticket text.

### Text Representation

**TF-IDF (Term Frequency-Inverse Document Frequency)** is used to convert text into numerical features.

### Classification Algorithm

**Logistic Regression** is used for classification.

Separate models are used for:

1. Ticket Category Prediction
2. Ticket Urgency Prediction

The trained models are stored using Joblib.

---

## 💻 Application Interface

The Streamlit application allows users to enter:

- Ticket ID
- Customer Name
- Customer Email
- Customer Issue

After clicking **Analyze Ticket**, the application displays:

- Predicted Category
- Predicted Urgency
- Assigned Support Team
- Category Confidence
- Urgency Confidence
- AI Explanation
- Routing Decision
- Ticket Information
- Ticket History
- Analytics Dashboard

---

## ▶️ How to Run the Project

### Step 1: Open the project folder

```bash
cd C:\Users\HP\Desktop\AI-Customer-Support-Ticket-Triage
```

### Step 2: Activate the virtual environment

```bash
venv2\Scripts\activate
```

### Step 3: Run the Streamlit application

```bash
streamlit run app\streamlit_app.py
```

### Step 4: Open the application

The Streamlit application will open in the browser.

---

## 🧪 Example

### Input

```text
My payment was charged twice and I need a refund.
```

### Output

```text
Category: Billing
Urgency: High
Assigned Team: Billing Support Team
```

The application also displays confidence scores, an AI explanation, and a routing decision.

---

## 👨‍💼 Human Review Mechanism

The system uses a confidence threshold of **70%**.

```text
Confidence ≥ 70%
        ↓
    Auto Route

Confidence < 70%
        ↓
Human Review Required
```

This allows uncertain tickets to be checked by a human.

---

## 📈 Benefits

- Reduces manual ticket classification effort.
- Helps prioritize customer issues.
- Supports faster ticket routing.
- Provides prediction transparency.
- Helps support teams monitor ticket patterns.
- Provides a simple user-friendly interface.

---

## ⚠️ Limitations

- The dataset contains a limited number of sample tickets.
- Prediction quality depends on the available training data.
- Ambiguous tickets may require human review.
- The project is currently a prototype and demonstration application.
- Ticket history is session-based and is not stored permanently in a database.

---

## 🚀 Future Scope

- Larger real-world customer support datasets.
- Advanced NLP and transformer-based models.
- Integration with real customer support platforms.
- Persistent database storage.
- Email and notification integration.
- Multilingual ticket classification.
- Advanced analytics and reporting.
- Continuous model retraining.

---

## 🎓 Project Information

**Project Type:** Academic AI & Machine Learning Project

**Domain:** Artificial Intelligence, Natural Language Processing and Customer Support Automation

---

## 👩‍💻 Developed By

**Sarmila V**

**Bachelor of Engineering – Computer Science and Engineering**

---

## 📄 License

This project is developed for academic and educational purposes.

This project is developed for academic and educational purposes.