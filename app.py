import streamlit as st
import ollama

# Page settings
st.set_page_config(
    page_title="AI",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("🤖 THE ULTIMATE")
st.write("Ask anything and get an answer.")

# Input box
prompt = st.text_input(
    "💬 Enter your question",
    placeholder="e.g. WHO AM I ?"
)

# Ask button
if st.button("🚀 Ask AI", use_container_width=True):

    if prompt.strip():

        with st.spinner("🤔 AI is thinking..."):

            response = ollama.chat(
                model="qwen2.5:0.5b",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

        # Display response
        st.subheader("🤖 AI Response")
        st.write(response["message"]["content"])

    else:
        st.warning("⚠️ Please enter a question first.")