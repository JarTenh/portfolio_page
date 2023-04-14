import streamlit as st


# Configure the page.
st.set_page_config(layout="wide")

# Create columns for the home page.
col1, col2 = st.columns(2)

# Open a column.
with col1:
    st.image("images/photo.jpeg", width=400)

with col2:
    st.title("Jarkko Tenhola")
    content = """
    Hi, I'm Jarkko! I am an eager-to-learn human being, interested in
    developing new skills to my repertoire. Currently exploring the
    world of python, and hopefully other programming languages in the
    future too!
    """
    st.info(content)
