import streamlit as st
import asyncio

from ai_app import ask_assistant

st.set_page_config(
    page_title="AI Utility Assistant"
)

st.title("AI Utlity Assistant")

st.write("Ask questions and interact with your AI assistant.")


if "messages" not in st.session_state:
    st.session_state.messages=[]


# displaying the previous messages
for messages in st.session_state.messages:
    with st.chat_message(messages['role']):
        st.write(messages['content'])

user_input=st.chat_input("Ask your question...")

if user_input :
    # Disply the user message

    st.session_state.messages.append({
        "role":"user",
        "content":user_input
    })
    with st.chat_message("user"):
        st.write(user_input)

    # Genrate assistant response
    with st.chat_message("assistant"):

        with st.spinner("Thinking"):

            try:
                answer=asyncio.run(ask_assistant(user_input))

                st.write(answer)

                st.session_state.messages.append({
                    "role":"assistant",
                    "content":answer
                }) 


            except Exception as e:
                st.write(f"Error : {str(e)}")


if st.button("Clear"):
    st.session_state.messages=[]
    st.rerun()







