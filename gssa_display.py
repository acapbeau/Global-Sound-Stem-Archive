import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="GSSA Archive Viewer", layout="wide")

st.title("🎵 Global Sound & Stem Archive")

# 1. Check if CSV exists
if not os.path.exists('metadata.csv'):
    st.error("❌ ERROR: 'metadata.csv' not found in this folder!")
    st.stop()

df = pd.read_csv('metadata.csv')

# 2. Display the Data
st.write("### Archive Items")

for index, row in df.iterrows():
    with st.container():
        st.subheader(f"{index + 1}. {row['Title']}")
        st.write(f"**Description:** {row['Description']}")
        
        # DEBUG: Let's see where the script thinks the file is
        file_path = row['Filename']
        
        if os.path.exists(file_path):
            st.audio(file_path)
            st.success(f"✅ Found: {file_path}")
        else:
            st.warning(f"⚠️ Missing File: I looked for '{file_path}' but couldn't find it.")
            st.info("Make sure your MP3s are inside a folder named 'items'.")
        
        st.divider()
