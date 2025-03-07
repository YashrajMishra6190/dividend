import streamlit as st

# Streamlit UI
st.title("Dividend Calculation")

# User inputs
x = st.number_input("Enter Opening Share Value in ₹:", min_value=0)
y = st.number_input("Enter New Share Value in ₹:", min_value=0)
month = st.number_input("Enter Month:", min_value=1, max_value=12)

# Calculate the result if the month is valid
if month > 12 or month < 1:
    st.error("Invalid Month")
else:
    result = 0.075 * (x + y * month / 12)
    st.write(f"Resultant for Dividend Calculation: ₹ {round(result)}")
