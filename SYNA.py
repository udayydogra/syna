import streamlit as st

def main(): 
    st.set_page_config(page_title="Syna", page_icon=":books:")
    st.header("Chat with multiple PDFs :books:")
    st.text_input("Ask the questions about your documents")
if __name__ == '__main__':
    main() 