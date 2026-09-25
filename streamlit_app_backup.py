import streamlit as st
import joblib
from pathlib import Path

# =========================================================
# PROJECT PATH
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

# =========================================================
# LOAD MODELS
# =========================================================

category_model = joblib.load(
    BASE_DIR / "models" / "category_model.pkl"
)

urgency_model = joblib.load(
    BASE_DIR / "models" / "urgency_model.pkl"
)

# =========================================================
# CONFIGURATION
# =========================================================

CONFIDENCE_THRESHOLD = 70

team_mapping = {
    "Billing": "Billing Support Team",
    "Account": "Account Support Team",
    "Technical": "Technical Support Team",
    "Product": "Product Support Team"
}

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Customer Support Ticket Triage",
    page_icon="🤖",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    .main {
        padding-top: 1rem;
    }

    .title-box {
        padding: 25px;
        border-radius: 15px;
        background: linear-gradient(
            135deg,
            #1f4e79,
            #2e75b6
        );
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

# =========================================================
# HEADER
# =========================================================

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

# =========================================================
# INPUT SECTION
# =========================================================

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

analyze = st.button(
    "🔍 Analyze Ticket",
    use_container_width=True
)
if st.button("🔄 Clear Form", use_container_width=True):
    st.rerun()

# =========================================================
# ANALYSIS
# =========================================================

if analyze:

    if not ticket.strip():

        st.warning(
            "⚠️ Please enter a customer support ticket."
        )

    else:

        # Category prediction
        category = category_model.predict([ticket])[0]

        # Urgency prediction
        urgency = urgency_model.predict([ticket])[0]

        # Confidence
        category_probabilities = (
            category_model.predict_proba([ticket])[0]
        )

        urgency_probabilities = (
            urgency_model.predict_proba([ticket])[0]
        )

        category_confidence = (
            max(category_probabilities) * 100
        )

        urgency_confidence = (
            max(urgency_probabilities) * 100
        )

        # Team assignment
        team = team_mapping.get(
            category,
            "General Support Team"
        )

        # Human review
        if (
            category_confidence < CONFIDENCE_THRESHOLD
            or urgency_confidence < CONFIDENCE_THRESHOLD
        ):
            decision = "Human Review Required"
        else:
            decision = "Auto Route"
                    # =================================================
        # AI EXPLANATION
        # =================================================

        if category == "Billing":
            category_reason = (
                "The ticket contains payment, charge, refund, "
                "invoice, or billing-related information."
            )

        elif category == "Account":
            category_reason = (
                "The ticket contains login, password, profile, "
                "or account-related information."
            )

        elif category == "Technical":
            category_reason = (
                "The ticket describes an application, website, "
                "server, loading, or technical problem."
            )

        elif category == "Product":
            category_reason = (
                "The ticket contains product-related information "
                "such as damage, return, quality, or product details."
            )

        else:
            category_reason = (
                "The ticket does not clearly match a predefined category."
            )

        if urgency == "High":
            urgency_reason = (
                "The issue appears urgent and may require immediate support."
            )

        elif urgency == "Medium":
            urgency_reason = (
                "The issue appears moderately important "
                "and may require timely support."
            )

        else:
            urgency_reason = (
                "The issue appears to be a general or informational request."
            )

        # =================================================
        # RESULTS
        # =================================================

        st.markdown(
            '<div class="section-title">📊 Prediction Results</div>',
            unsafe_allow_html=True
        )

        col1, col2 = st.columns(2)

        with col1:

            st.markdown(
                f"""
                <div class="result-card">
                    <div class="result-label">
                        Category
                    </div>
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
                    <div class="result-label">
                        Urgency
                    </div>
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
                    <div class="result-label">
                        Assigned Team
                    </div>
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
        # =================================================
        # AI EXPLANATION DISPLAY
        # =================================================

        st.markdown(
            '<div class="section-title">💡 AI Explanation</div>',
            unsafe_allow_html=True
        )

        st.info(
            f"🏷️ **Category Reason:** {category_reason}\n\n"
            f"🚨 **Urgency Reason:** {urgency_reason}"
        )

        # =================================================
        # DECISION
        # =================================================

        st.markdown(
            '<div class="section-title">⚡ Routing Decision</div>',
            unsafe_allow_html=True
        )

        if decision == "Human Review Required":

            st.warning(
                "👨‍💼 Human Review Required\n\n"
                "The AI confidence is below the 70% threshold."
            )

        else:

            st.success(
                "✅ Auto Route\n\n"
                "The AI confidence is high enough for automatic routing."
            )

# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        AI Customer Support Ticket Triage System |
        Python • Scikit-learn • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)