import streamlit as st
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "tickets.csv"

CONFIDENCE_THRESHOLD = 70
# Ticket History
if "ticket_history" not in st.session_state:
    st.session_state.ticket_history = []

team_mapping = {
    "Billing": "Billing Support Team",
    "Account": "Account Support Team",
    "Technical": "Technical Support Team",
    "Product": "Product Support Team"
}


# -----------------------------
# Simple AI-style text analysis
# -----------------------------

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


category_keywords = {
    "Billing": [
        "payment", "charged", "charge", "refund", "invoice",
        "bill", "billing", "price", "receipt", "card", "paid"
    ],
    "Account": [
        "login", "password", "account", "profile", "sign",
        "credentials", "email", "phone", "locked", "blocked",
        "reset"
    ],
    "Technical": [
        "app", "application", "website", "server", "error",
        "crash", "crashing", "slow", "loading", "freeze",
        "freezes", "software", "connection", "technical"
    ],
    "Product": [
        "product", "item", "order", "damaged", "broken",
        "return", "quality", "wrong item", "received",
        "details"
    ]
}


def predict_category(ticket):
    text = clean_text(ticket)

    scores = {}

    for category, keywords in category_keywords.items():
        score = 0

        for keyword in keywords:
            if keyword in text:
                score += 1

        scores[category] = score

    best_category = max(scores, key=scores.get)
    best_score = scores[best_category]

    total_score = sum(scores.values())

    if best_score == 0:
        return "Product", 40.0

    confidence = 55 + (
        best_score / max(total_score, best_score)
    ) * 40

    confidence = min(confidence, 95)

    return best_category, confidence


def predict_urgency(ticket):
    text = clean_text(ticket)

    high_keywords = [
        "urgent", "emergency", "immediately", "cannot",
        "can't", "failed", "failure", "blocked", "locked",
        "broken", "crashed", "crashing", "down", "twice",
        "unknown charge", "not working"
    ]

    medium_keywords = [
        "slow", "late", "pending", "refund",
        "return", "change", "incorrect", "problem"
    ]

    high_score = sum(
        1 for keyword in high_keywords
        if keyword in text
    )

    medium_score = sum(
        1 for keyword in medium_keywords
        if keyword in text
    )

    if high_score > 0:
        urgency = "High"
        confidence = min(60 + high_score * 8, 92)

    elif medium_score > 0:
        urgency = "Medium"
        confidence = min(60 + medium_score * 7, 88)

    else:
        urgency = "Low"
        confidence = 78.0

    return urgency, confidence


def get_category_reason(category):
    reasons = {
        "Billing":
            "The ticket contains payment, charge, refund, invoice, "
            "or billing-related information.",

        "Account":
            "The ticket contains login, password, profile, "
            "or account-related information.",

        "Technical":
            "The ticket describes an application, website, server, "
            "loading, or technical problem.",

        "Product":
            "The ticket contains product-related information "
            "such as damage, return, quality, or product details."
    }

    return reasons.get(
        category,
        "The ticket does not clearly match a predefined category."
    )


def get_urgency_reason(urgency):
    reasons = {
        "High":
            "The issue appears urgent and may require immediate support.",

        "Medium":
            "The issue appears moderately important and may require "
            "timely support.",

        "Low":
            "The issue appears to be a general or informational request."
    }

    return reasons.get(urgency, "")


# -----------------------------
# Streamlit configuration
# -----------------------------

st.set_page_config(
    page_title="AI Customer Support Ticket Triage",
    page_icon="🤖",
    layout="wide"
)


# -----------------------------
# Professional UI
# -----------------------------

st.markdown(
    """
    <style>

    .main {
        padding-top: 1rem;
    }

    .title-box {
        padding: 25px;
        border-radius: 15px;
        background: linear-gradient(135deg,#1f4e79,#2e75b6);
        color: white;
        text-align: center;
        margin-bottom: 25px;
    }

    .title-box h1 {
        font-size: 38px;
        margin-bottom: 8px;
    }

    .title-box p {
        font-size: 17px;
        margin: 0;
    }

    .section-title {
        font-size: 22px;
        font-weight: bold;
        margin-top: 15px;
        margin-bottom: 10px;
    }

    .result-card {
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #d9e2f3;
        background-color: #f8fbff;
        margin-bottom: 12px;
    }

    .result-label {
        font-size: 14px;
        color: #666666;
    }

    .result-value {
        font-size: 21px;
        font-weight: bold;
    }

    .footer {
        text-align: center;
        color: #777777;
        font-size: 13px;
        margin-top: 35px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Header
# -----------------------------

st.markdown(
    """
    <div class="title-box">
        <h1>🤖 AI Customer Support Ticket Triage</h1>
        <p>
            Intelligent ticket classification, prioritization
            and support team routing
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Input section
# -----------------------------

st.markdown(
    '<div class="section-title">🎫 Customer Support Ticket</div>',
    unsafe_allow_html=True
)

ticket_id = st.text_input(
    "🎫 Ticket ID",
    placeholder="Example: TKT-1001"
)

customer_name = st.text_input(
    "👤 Customer Name",
    placeholder="Example: Sarmila"
)

customer_email = st.text_input(
    "📧 Customer Email",
    placeholder="Example: customer@email.com"
)

ticket = st.text_area(
    "Enter the customer's issue below:",
    placeholder=(
        "Example: My payment was charged twice "
        "and I need help with a refund."
    ),
    height=150
)


# -----------------------------
# Buttons
# -----------------------------

col_button1, col_button2 = st.columns(2)

with col_button1:
    analyze = st.button(
        "🔍 Analyze Ticket",
        use_container_width=True
    )

with col_button2:
    clear = st.button(
        "🔄 Clear Form",
        use_container_width=True
    )

if clear:
    st.rerun()


# -----------------------------
# Analysis
# -----------------------------

if analyze:

    if not ticket.strip():

        st.warning(
            "⚠️ Please enter a customer support ticket."
        )

    else:

        category, category_confidence = predict_category(ticket)

        urgency, urgency_confidence = predict_urgency(ticket)

        team = team_mapping.get(
            category,
            "General Support Team"
        )
                 

         
        if (
            category_confidence < CONFIDENCE_THRESHOLD
            or urgency_confidence < CONFIDENCE_THRESHOLD
        ):
            decision = "Human Review Required"

        if (
            category_confidence < CONFIDENCE_THRESHOLD
            or urgency_confidence < CONFIDENCE_THRESHOLD
        ):
            decision = "Human Review Required"
        else:
            decision = "Auto Route"
                     
        # Save ticket to history
        st.session_state.ticket_history.append({
            "Ticket ID": ticket_id,
            "Customer": customer_name,
            "Category": category,
            "Urgency": urgency,
            "Assigned Team": team,
            "Category Confidence": round(category_confidence, 2),
            "Urgency Confidence": round(urgency_confidence, 2),
            "Decision": decision
        })

        category_reason = get_category_reason(category)

        urgency_reason = get_urgency_reason(urgency)


        # -----------------------------
        # Prediction Results
        # -----------------------------

        st.markdown(
            '<div class="section-title">📊 Prediction Results</div>',
            unsafe_allow_html=True
        )


        col1, col2 = st.columns(2)

        with col1:

            st.markdown(
                f"""
                <div class="result-card">
                    <div class="result-label">Category</div>
                    <div class="result-value">
                        🏷️ {category}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


        with col2:

            st.markdown(
                f"""
                <div class="result-card">
                    <div class="result-label">Urgency</div>
                    <div class="result-value">
                        🚨 {urgency}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


        col3, col4 = st.columns(2)

        with col3:

            st.markdown(
                f"""
                <div class="result-card">
                    <div class="result-label">Assigned Team</div>
                    <div class="result-value">
                        👥 {team}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


        with col4:

            st.markdown(
                f"""
                <div class="result-card">
                    <div class="result-label">
                        Category Confidence
                    </div>
                    <div class="result-value">
                        📈 {category_confidence:.2f}%
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-label">
                    Urgency Confidence
                </div>
                <div class="result-value">
                    📈 {urgency_confidence:.2f}%
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


        # -----------------------------
        # AI Explanation
        # -----------------------------

        st.markdown(
            '<div class="section-title">💡 AI Explanation</div>',
            unsafe_allow_html=True
        )

        st.info(
            f"🏷️ **Category Reason:** {category_reason}\n\n"
            f"🚨 **Urgency Reason:** {urgency_reason}"
        )


        # -----------------------------
        # Routing Decision
        # -----------------------------

        st.markdown(
            '<div class="section-title">⚡ Routing Decision</div>',
            unsafe_allow_html=True
        )


        if decision == "Human Review Required":

            st.warning(
                "👨‍💼 **Human Review Required**\n\n"
                "The AI confidence is below the 70% threshold."
            )

        else:

            st.success(
                "✅ **Auto Route**\n\n"
                "The AI confidence is high enough for automatic routing."
            )


        # -----------------------------
        # Ticket information
        # -----------------------------

        if ticket_id or customer_name or customer_email:

            st.markdown(
                '<div class="section-title">📋 Ticket Information</div>',
                unsafe_allow_html=True
            )

            info_text = ""

            if ticket_id:
                info_text += f"**Ticket ID:** {ticket_id}  \n"

            if customer_name:
                info_text += f"**Customer:** {customer_name}  \n"

            if customer_email:
                info_text += f"**Email:** {customer_email}"

            st.info(info_text)


# -----------------------------
# Footer
# -----------------------------

st.markdown(
    """
    <div class="footer">
        AI Customer Support Ticket Triage System |
        Python • NLP • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
# -----------------------------
# Ticket History
# -----------------------------

st.markdown(
    '<div class="section-title">📜 Ticket History</div>',
    unsafe_allow_html=True
)

if st.session_state.ticket_history:
    st.dataframe(
        st.session_state.ticket_history,
        use_container_width=True
    )
else:
    st.info("No ticket history available yet.")
    # -----------------------------
# Analytics Dashboard
# -----------------------------

st.markdown(
    '<div class="section-title">📊 Analytics Dashboard</div>',
    unsafe_allow_html=True
)

if st.session_state.ticket_history:

    total_tickets = len(st.session_state.ticket_history)

    billing_count = sum(
        1 for t in st.session_state.ticket_history
        if t["Category"] == "Billing"
    )

    account_count = sum(
        1 for t in st.session_state.ticket_history
        if t["Category"] == "Account"
    )

    technical_count = sum(
        1 for t in st.session_state.ticket_history
        if t["Category"] == "Technical"
    )

    product_count = sum(
        1 for t in st.session_state.ticket_history
        if t["Category"] == "Product"
    )

    high_count = sum(
        1 for t in st.session_state.ticket_history
        if t["Urgency"] == "High"
    )

    medium_count = sum(
        1 for t in st.session_state.ticket_history
        if t["Urgency"] == "Medium"
    )

    low_count = sum(
        1 for t in st.session_state.ticket_history
        if t["Urgency"] == "Low"
    )

    auto_route_count = sum(
        1 for t in st.session_state.ticket_history
        if t["Decision"] == "Auto Route"
    )

    human_review_count = sum(
        1 for t in st.session_state.ticket_history
        if t["Decision"] == "Human Review Required"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🎫 Total Tickets", total_tickets)

    with col2:
        st.metric("🤖 Auto Routed", auto_route_count)

    with col3:
        st.metric("👨‍💼 Human Review", human_review_count)

    st.markdown("### 🏷️ Tickets by Category")

    category_data = {
        "Billing": billing_count,
        "Account": account_count,
        "Technical": technical_count,
        "Product": product_count
    }

    st.bar_chart(category_data)

    st.markdown("### 🚨 Tickets by Urgency")

    urgency_data = {
        "High": high_count,
        "Medium": medium_count,
        "Low": low_count
    }

    st.bar_chart(urgency_data)

else:
    st.info("Analyze tickets to generate analytics.")