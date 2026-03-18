import streamlit as st

st.set_page_config(page_title="FinServe AI Support Assistant", page_icon="🤖")

FAQ_RESPONSES = {
    "loan status": "Your loan application is currently under review. You will receive an update soon.",
    "documents": "You may need ID, financial statements, and proof of business activity.",
    "repayment": "You can check your repayment schedule in the client portal.",
    "interest": "Interest rates depend on your profile and risk assessment.",
    "kyc": "KYC is a process to verify your identity for compliance.",
}

def generate_response(user_query):
    query = user_query.lower()

    if "status" in query:
        return FAQ_RESPONSES["loan status"]
    elif "document" in query:
        return FAQ_RESPONSES["documents"]
    elif "repayment" in query:
        return FAQ_RESPONSES["repayment"]
    elif "interest" in query:
        return FAQ_RESPONSES["interest"]
    elif "kyc" in query:
        return FAQ_RESPONSES["kyc"]
    else:
        return "Thank you for your message. Please contact support for more details."

st.title("🤖 FinServe AI Support Assistant")

user_input = st.text_area("Ask a question:")

if st.button("Generate Response"):
    if user_input:
        response = generate_response(user_input)

        st.subheader("Assistant Response")
        st.success(response)