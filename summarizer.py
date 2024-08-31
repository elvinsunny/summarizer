


import streamlit as st
from transformers import pipeline

# Initialize the summarization pipeline with the specified model
summarizer = pipeline("summarization", model="Falconsai/text_summarization")

# Set the title and description of the Streamlit app
st.set_page_config(page_title="Text Summarizer", page_icon="📝")
st.title("📝 Text Summarizer")
st.write("A simple app to summarize text using a state-of-the-art model.")

# Add a sidebar for configuration
st.sidebar.header("Summary Settings")
min_length = st.sidebar.slider("Select minimum summary length", min_value=10, max_value=100, value=30)
max_length = st.sidebar.slider("Select maximum summary length", min_value=50, max_value=200, value=130)

# Create a text area for user input
st.write("## Input Text")
text = st.text_area("Enter the text you want to summarize:", height=200)

# Add a button to trigger the summarization
if st.button("Summarize"):
    if text:
        with st.spinner("Generating summary..."):
            # Generate summary
            summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
            st.success("Summary generated successfully!")
            st.write("### Summary")
            st.write(summary[0]['summary_text'])
    else:
        st.warning("Please enter text to summarize.")

# Footer
st.write("---")
st.write("Made with ❤️ using [Hugging Face Transformers](https://huggingface.co/docs/transformers/index) and [Streamlit](https://streamlit.io/)")






