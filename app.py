import streamlit as st
from gpt_service import generate_answer
from guard_service import check_input, check_validity_by_llm

def main():
    st.title("Masai Chatbot")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    query = st.chat_input("Ask your question?")

    if query:
        with st.chat_message("human"):
            st.markdown(query)

        st.session_state.messages.append({"role": "user", "content" : query})

        is_valid = check_validity_by_llm(query)

        if not is_valid["valid"]:
            with st.chat_message("assistant"):
                 st.markdown(f"POLICY VIOLATION REPORTED : {is_valid["reason"]}")
            st.session_state.messages.append({"role": "assistant", "content": is_valid["reason"]})
        else:
            response = generate_answer(st.session_state.messages)
            with st.chat_message("ai"):
                st.markdown(response)

            st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()