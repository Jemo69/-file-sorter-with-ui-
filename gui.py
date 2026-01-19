import streamlit as st
import os
from sorter import sorter

def GUI():
    # Page configuration
    st.set_page_config(page_title="File Sorter", layout="centered")

    st.title("File Sorter")
    st.write("Organize your files by entering the directory path below.")

    # Input field for the directory path
    # Defaulting to the current working directory
    default_path = os.getcwd()
    dir_path = st.text_input("Directory Path:", value=default_path)

    # Sort Button
    if st.button("Sort Files"):
                # Call your custom sorter function
                sorter(dir_path)
                
                # Show success message
                st.success(f"Successfully sorted files in: {dir_path}")
                st.balloons()

if __name__ == "__main__":
    GUI()
