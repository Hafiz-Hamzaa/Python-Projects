import streamlit as st
import re  # Regular expressions module

st.title("🔐 Password Strength Meter")
st.write("Enter your password below to check its strength.")

# User se password input lena
password = st.text_input("Enter your password", type="password")

# Button to check password strength
if st.button("Check Password Strength"):
    if len(password) < 8:
        st.write("❌ Weak Password: Must be at least 8 characters long.")
        st.progress(0)  # 0% progress
    else:
        # Initialize score
        score = 0
        
        # Checking different conditions
        if re.search(r'[a-z]', password):
            score += 1  # Lowercase letter present
        
        if re.search(r'[A-Z]', password):
            score += 1  # Uppercase letter present
        
        if re.search(r'[0-9]', password):
            score += 1  # Number present
        
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            score += 1  # Special character present

        # Calculate progress percentage
        progress_percentage = score / 4  # Convert score to percentage (0 to 1)
        
        # Show progress bar
        st.progress(progress_percentage)  # Show bar based on strength

        # Display score-based feedback
        if score == 1:
            st.write("❌ Weak Password: Try adding more variety (uppercase, numbers, special characters).")
        elif score == 2:
            st.write("⚠️ Moderate Password: Add more characters for better security.")
        elif score == 3:
            st.write("✅ Good Password: Almost strong, try adding a special character.")
        else:
            st.write("🔥 Strong Password: Your password is very secure!")