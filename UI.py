

#-----------------------------------------------------------------------streamlit ui for the chatbot ------------------------------------------------------------
import streamlit as st

st.title("Bangla Literature Q&A Bot")

user_query = st.text_input("Enter your question here:")

if user_query:
    with st.spinner("Generating answer..."):
        answer = generate_answer(user_query, st.session_state.short_term_memory)
    st.markdown("**Answer:**")
    st.write(answer)

# Sidebar for chat history
st.sidebar.title("Previous Chat History")
if st.session_state.short_term_memory:
    for chat in reversed(st.session_state.short_term_memory):
        st.sidebar.markdown(chat)
else:
    st.sidebar.write("No previous chats yet.")
    
    
    
    
