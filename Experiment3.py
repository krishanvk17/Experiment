import streamlit as st
st.set_page_config(page_title = "New Tab",
                          page_icon = "🤫",
                          layout = 'centered',
                          initial_sidebar_state = 'auto')
username1="krishanvk"
password1="vk"
if st.button("Log in"):
    if st.text_input("Username")==username1 and st.text_input("Password")==password1:
        ")
