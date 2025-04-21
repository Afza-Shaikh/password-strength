import streamlit as st
import re
import random

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ At least 8 characters required.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one digit (0–9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    if len(password) >= 12:
        score += 1  # bonus point for long password

    return score, feedback

def generate_strong_password(length=12):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

# --------- Streamlit UI ---------
st.set_page_config(page_title="🔐 Password Strength Meter", page_icon="🔐")

st.title("🔐 Password Strength Meter")
st.write("Check how strong your password is and get tips to improve it.")

option = st.radio("Choose an option:", ["Check a password", "Generate strong password"])

if option == "Check a password":
    password = st.text_input("Enter your password", type="password")

    if st.button("Check Strength"):
        if password:
            score, feedback = check_password_strength(password)
            
            if score >= 5:
                st.success("✅ Strong Password!")
            elif score >= 3:
                st.warning("⚠️ Moderate Password - Can be improved.")
            else:
                st.error("❌ Weak Password - Needs improvement.")

            st.markdown("### Feedback:")
            for tip in feedback:
                st.write("- " + tip)
        else:
            st.warning("Please enter a password.")

elif option == "Generate strong password":
    length = st.slider("Select password length", 8, 20, 12)
    new_password = generate_strong_password(length)
    st.text_input("Generated Password:", value=new_password)
    st.info("Copy this password and use it safely!")

