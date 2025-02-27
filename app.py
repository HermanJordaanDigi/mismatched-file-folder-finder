import streamlit as st
import os
import re

def scan_directory(base_dir):
    """
    Walks through the directory tree starting at base_dir.
    For each folder, checks files with extensions (.jpg, .jpeg, .png, .eip)
    to see if their base name matches the parent folder name followed by an underscore and exactly three digits.
    Returns a set of folder paths that contain at least one mismatched file.
    """
    mismatched_folders = set()
    
    for root, dirs, files in os.walk(base_dir):
        if not files:
            continue
        
        folder_name = os.path.basename(root)
        for f in files:
            file_path = os.path.join(root, f)
            if not os.path.isfile(file_path):
                continue
            
            name, ext = os.path.splitext(f)
            if ext.lower() not in ['.jpg', '.jpeg', '.png', '.eip']:
                continue
            
            # Regex: folderName_ followed by exactly 3 digits
            pattern = r'^' + re.escape(folder_name) + r'_\d{3}$'
            if not re.fullmatch(pattern, name):
                mismatched_folders.add(root)
                break
    
    return mismatched_folders

st.title("Mismatched File & Folder Finder  📂")
st.markdown('<span style="color:orange;">_by <a href="https://www.herman-jordaan.com/" style="color:orange;">Herman Jordaan Digi ©</a>_</span>', unsafe_allow_html=True)
st.write("Enter the directory path you want to scan:")

directory = st.text_input("Directory Path", value="")

if st.button("Scan Directory"):
    if not directory:
        st.error("Please provide a directory path.")
    elif not os.path.isdir(directory):
        st.error("The provided path is not a valid directory.")
    else:
        mismatched_folders = scan_directory(directory)
        if not mismatched_folders:
            st.success("No mismatches found!")
        else:
            # Bold and orange header text.
            st.markdown('<span style="color:orange; font-weight:bold;">Folders with mismatched files:</span>', unsafe_allow_html=True)
            for folder in sorted(mismatched_folders):
                # Extract the folder's base name and its parent directory.
                folder_name = os.path.basename(folder)
                parent_dir = os.path.dirname(folder)
                
                # Highlight only the folder's name in orange.
                highlighted_folder_name = f'<span style="color:orange; font-weight:bold;">{folder_name}</span>'
                if parent_dir:
                    output = f"{parent_dir}/{highlighted_folder_name}"
                else:
                    output = highlighted_folder_name
                
                st.markdown(output, unsafe_allow_html=True)
