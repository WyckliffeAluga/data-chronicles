from glob import glob
import librosa as lr
import matplotlib.pyplot as plt
import numpy as np

from librosa.core import stft , amplitude_to_db
from librosa.display import specshow

audio_files = glob("datasets/files/set_a/*.wav")

# Read in the first audio file, create the time array
audio, sfreq = lr.load(audio_files[3])

# calculate our STFT
HOP_LENGTH = 2 ** 4
SIZE_WINDOW = 2 ** 7
audio_spec = stft(audio, hop_length=HOP_LENGTH, n_fft=SIZE_WINDOW)

# convert into decibels
spec  = amplitude_to_db(audio_spec)

# Visualize
specshow(spec, sr=sfreq, x_axis="time",
        y_axis="hz",hop_length=HOP_LENGTH)

# calculate spectral features
bandwidth = lr.feature.spectral_bandwidth(S=np.abs(spec))[0]
centroids = lr.feature.spectral_centroid(S=np.abs(spec))[0]


# display these features on top of the spectrogram
ax = specshow(spec, x_axis="time" , y_axis="hz", hop_length=HOP_LENGTH)
ax.plot(times, centroids)
ax.fill_between(times, centroids - bandwidths / 2, centroids + bandwidths /2 , alpha=0.5)


# combining spectral and temporal features in classifier

centroids_all = []
bandwidths_all = []

for spec in spectrograms:
    bandwidths  = lr.feature.spectral_bandwidth(S=lr.db_to_amplitude(spec))
    centroids   = lr.feature.spectral_centroids(S=lr.db_to_amplitude(spec))

    # calculates the mean spectral bandwidth
    bandwidths_all.append(np.mean(bandwidths))

    # calculate the mean spectral centroid
    centroids_all.append(np.mean(centroids))


# create our X matrix
X = np.column_stack([means, stds, maxs, tempo_mean, tempo_max, tempo_std,
                    bandwidths_all, centroids_all])
