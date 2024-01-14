import streamlit as st

def contact_form():
    st.subheader("Contact Us")
    
    # Input fields for name, email, and message
    name = st.text_input("Your Name:")
    email = st.text_input("Your Email:")
    message = st.text_area("Your Message:")

    # Submit button
    if st.button("Submit"):
        st.success("Message Sent!")
        st.write(f"Name: {name}")
        st.write(f"Email: {email}")
        st.write(f"Message: {message}")
        st.balloons()

# Streamlit App
st.title("Contact Form Example")

# Display the contact form
contact_form()

