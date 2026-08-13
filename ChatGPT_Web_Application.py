from __future__ import annotations

import os

import streamlit as st

from openai_service import DEFAULT_MODEL, generate_response

st.set_page_config(
    page_title="ChatGPT-style Responses API Demo",
    page_icon="💬",
)

st.title("ChatGPT-style Web Application")
st.caption("Modern OpenAI Responses API + Streamlit")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "previous_response_id" not in st.session_state:
    st.session_state.previous_response_id = None

if "active_model" not in st.session_state:
    st.session_state.active_model = DEFAULT_MODEL

with st.sidebar:
    st.header("Settings")
    model = st.text_input(
        "Model",
        value=st.session_state.active_model,
        help="Default comes from OPENAI_MODEL or falls back to gpt-5.5.",
    ).strip()

    if not model:
        model = DEFAULT_MODEL

    if model != st.session_state.active_model:
        st.session_state.active_model = model
        st.session_state.previous_response_id = None
        st.session_state.messages = []
        st.info("Conversation reset because the model changed.")

    if st.button("Clear conversation", use_container_width=True):
        st.session_state.messages = []
        st.session_state.previous_response_id = None
        st.rerun()

    st.markdown("---")
    if os.getenv("OPENAI_API_KEY"):
        st.success("OPENAI_API_KEY detected.")
    else:
        st.warning("Set OPENAI_API_KEY in the environment before sending a message.")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask something...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                answer, response_id = generate_response(
                    prompt,
                    model=st.session_state.active_model,
                    previous_response_id=st.session_state.previous_response_id,
                )
            st.markdown(answer)

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )
        st.session_state.previous_response_id = response_id

    except Exception as exc:
        st.error(f"OpenAI request failed: {type(exc).__name__}: {exc}")
