import librosa
import os
import pandas as pd

# Your specific uploaded files
files = [
    'INST BASS.wav', 
    'INST KEYS.wav', 
    'INST MAIN #01_bip_1 (Drums)_1.wav', 
    'INST MAIN #01_bip_1 (Guitar)_2.wav', 
    'INST MAIN #01_bip_1 (Guitar).wav'
]

data = []

for file in files:
    if os.path.exists(file):
        print(f"Analyzing {file}...")
        y, sr = librosa.load(file)
        
        # Audio Analysis
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
        key_index = chroma.mean(axis=1).argmax()
        notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        
        data.append({
            'Title': file.replace('.wav', ''),
            'Creator': 'Bobo Mpeti',
            'Date': '2025-05-01',
            'BPM': 93, # Hardcoded per your project specs
            'Key': 'E', # Hardcoded per your project specs
            'Subject': 'Instrumental Stems',
            'Format': 'WAV',
            'Language': 'Instrumental',
            'Keywords': 'Afropop, Congolese, UK, Afrohouse',
            'Rights': '© Bobo Mpeti'
        })

# Export to CSV
df = pd.DataFrame(data)
df.to_csv('metadata.csv', index=False)
print("metadata.csv created successfully.")