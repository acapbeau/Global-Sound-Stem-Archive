import streamlit as st
import pandas as pd
import os

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Global Sound & Stem Archive (GSSA)",
    page_icon="🎵",
    layout="wide"
)

# --- CUSTOM CSS FOR AESTHETICS ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #1e2130; padding: 15px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("🎵 Global Sound & Stem Archive (GSSA)")
st.subheader("Digital Curation & Preservation Project | INFO 4730")
st.markdown("---")

# --- SIDEBAR / PROJECT INFO ---
st.sidebar.header("Project Details")
st.sidebar.info("""
**Creator:** Bobo Mpeti  
**Project:** Fan Club  
**Key:** E Major  
**BPM:** 93  
**Genre:** Afropop / Congolese
""")

st.sidebar.divider()
st.sidebar.write("### Instructions")
st.sidebar.write("1. Ensure your `.wav` files are in an `items/` folder.")
st.sidebar.write("2. Ensure `metadata.csv` is in the same directory.")

# --- LOAD DATA ---
@st.cache_data
def load_data():
    # If metadata.csv doesn't exist, create a temporary one for the display
    if os.path.exists('metadata.csv'):
        return pd.read_csv('metadata.csv')
    else:
        # Fallback data based on your specific uploaded files
        data = {
            'Title': ['INST BASS', 'INST KEYS', 'Drums (Main)', 'Guitar (Leads)', 'Guitar (Rhythm)'],
            'Filename': [
                'items/INST BASS.wav', 
                'items/INST KEYS.wav', 
                'items/INST MAIN #01_bip_1 (Drums)_1.wav', 
                'items/INST MAIN #01_bip_1 (Guitar)_2.wav', 
                'items/INST MAIN #01_bip_1 (Guitar).wav'
            ],
            'Keywords': ['Afropop', 'Amapiano', 'Congolese', 'UK House', 'Afrohouse']
        }
        return pd.DataFrame(data)

df = load_data()

# --- SEARCH BAR ---
search_query = st.text_input("🔍 Search Archive (e.g., 'Bass', 'Guitar', 'Drums')", "")

# --- FILTERING LOGIC ---
if search_query:
    filtered_df = df[df.apply(lambda row: search_query.lower() in row.astype(str).str.lower().values, axis=1)]
else:
    filtered_df = df

# --- DISPLAY ITEMS ---
st.write(f"### Accessing **{len(filtered_df)}** Items in Archive")

for index, row in filtered_df.iterrows():
    with st.expander(f"▶️ {row['Title']}", expanded=True):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"**Metadata Tags:** `{row['Keywords']}`")
            # Path logic: checking if file is local or in /items
            file_path = row['Filename']
            if os.path.exists(file_path):
                st.audio(file_path)
            else:
                st.warning(f"Audio file '{file_path}' not found in the project directory.")
        
        with col2:
            st.button(f"Download Metadata for Item {index+1}", key=f"btn_{index}")
            st.caption("Format: WAV | Bit Depth: 24-bit")

# --- FOOTER ---
st.markdown("---")
st.caption("Global Sound & Stem Archive © 2026 | Preservation through Digital Curation")