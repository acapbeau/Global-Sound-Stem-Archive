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
    data.append({
        'Title': file.replace('.mp3', ''),
        'Filename': f"items/{file}",
        'Creator': 'Bobo Mpeti',
        'Date': '2025-05-01',
        'BPM': 93,
        'Key': 'E',
        'Subject': 'Instrumental Stems (Proxy)',
        'Format': 'MP3',
        'Language': 'Instrumental',
        'Keywords': 'Afropop, Congolese, UK, Afrohouse',
        'Rights': '© Bobo Mpeti'
    })

# Export to CSV
df = pd.DataFrame(data)
df.to_csv('metadata.csv', index=False)
print("Updated metadata.csv created with MP3 file references.")
df = pd.DataFrame(data)
df.to_csv('metadata.csv', index=False)
print("metadata.csv created successfully.")
