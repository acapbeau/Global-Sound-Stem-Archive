import pandas as pd

# Your specific uploaded .mp3 files
files = [
    'INST BASS.mp3', 
    'INST KEYS.mp3', 
    'INST MAIN  01_bip_1 (Drums)_1.mp3', 
    'INST MAIN  01_bip_1 (Guitar)_2.mp3', 
    'INST MAIN  01_bip_1 (Guitar).mp3'
]

data = []

for file in files:
    # Creating a more descriptive label based on the filename
    clean_title = file.replace('.mp3', '').replace('INST ', '').replace('MAIN  01_bip_1 ', '')
    
    data.append({
        'Title': file.replace('.mp3', ''),
        'Filename': f"items/{file}",
        'Creator': 'Bobo Mpeti',
        'Date': '2025-05-01',
        'BPM': 93,
        'Key': 'E',
        'Description': f"High-quality instrumental stem for the project 'Fan Club'. Captured in Logic Pro. Key: E Major, Tempo: 93 BPM. This MP3 serves as a preview proxy for the archival WAV master.",
        'Subject': 'Music Production Stems',
        'Format': 'MP3',
        'Language': 'Instrumental',
        'Keywords': 'Afropop, Congolese, UK, Afrohouse, Logic Pro, Stems',
        'Rights': '© 2026 Bobo Mpeti. All rights reserved. Citation required for research use.'
    })

# Export to CSV
df = pd.DataFrame(data)
df.to_csv('metadata.csv', index=False)
print("Metadata CSV successfully updated with detailed descriptions.")
