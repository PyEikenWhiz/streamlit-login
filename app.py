import streamlit as st

# Create a title for the app
st.title("Login Sample App")

# Add a text input field for the username
username = st.text_input(label="Username", placeholder="Enter your username here...")

# Add a text input field for the password
password = st.text_input(label="Password", type="password", placeholder="Enter your password here...")

# Add a submit button
submit = st.button(label="Submit")

if submit:
    # Check if the user entered valid credentials
    if username == "admin" and password == "123456":
        st.write("Welcome, admin! You have successfully logged in.")
    else:
        st.write("Invalid credentials. Please try again.")
else:
    st.write("Please enter both a username and password to log in.")
