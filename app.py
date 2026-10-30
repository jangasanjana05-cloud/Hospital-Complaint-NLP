import streamlit as st
from backend import predict_complaint

st.set_page_config(
    page_title="Hospital Complaint NLP",
    page_icon="🏥"
)

st.title("🏥 Hospital Complaint Classification")
st.subheader("Complaint Category and Priority Prediction")

st.write("Enter a hospital complaint below.")

complaint = st.text_area(
    "Enter Hospital Complaint",
    placeholder="Type your complaint here..."
)

if st.button("Predict"):
    if complaint.strip():
        category, priority = predict_complaint(complaint)

        st.success("Prediction completed!")
        st.write("**Complaint Category:**", category)
        st.write("**Priority:**", priority)
    else:
        st.warning("Please enter a complaint.")
