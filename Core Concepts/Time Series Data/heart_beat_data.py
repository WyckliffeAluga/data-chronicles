from glob import glob
import librosa as lr
import matplotlib.pyplot as plt
import numpy as np

audio_files = glob("datasets/files/set_a/*.wav")

# Read in the first audio file, create the time array
audio, sfreq = lr.load(audio_files[3])
time = np.arange(0, len(audio)) / sfreq

# Plot audio over time
fig, ax = plt.subplots()
ax.plot(time, audio)
ax.set(xlabel='Time (s)', ylabel='Sound Amplitude')
plt.show()
