import streamlit as st

st.title("Simple Interest Calculator")

principal = st.number_input("Enter Principal Amount", min_value=0.0)
rate = st.number_input("Enter Rate of Interest (%)", min_value=0.0)
time = st.number_input("Enter Time Period (Years)", min_value=0.0)

if st.button("Calculate"):
    simple_interest = (principal * rate * time) / 100
    st.success(f"Simple Interest: {simple_interest:.2f}")