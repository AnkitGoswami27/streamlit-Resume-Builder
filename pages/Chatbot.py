import openai
import streamlit as st

# Set your OpenAI API key from Streamlit secrets
api_key = st.secrets["OPENAI_API_KEY"]

# Initialize OpenAI API client with the API key
openai.api_key = api_key

# Set a default model
default_model = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.expander(message["role"]):
        st.text(message["content"])

# Accept user input
user_input = st.text_input("You:")
if st.button("Send"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "User", "content": user_input})

    try:
        # Call OpenAI API for chat completion
        response = openai.ChatCompletion.create(
            model=default_model,
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
        )

        # Get and display assistant response
        assistant_response = response.choices[0].message["content"]
        st.session_state.messages.append({"role": "Assistant", "content": assistant_response})

        # Display assistant response
        with st.expander("Assistant"):
            st.text(assistant_response)

    except openai.error.OpenAIError as e:
        # Handle OpenAI API errors
        st.error(f"OpenAI API Error: {e}")
