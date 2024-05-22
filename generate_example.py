"""Example to generate a wind noise signal."""

import numpy as np
from sc_wind_noise_generator import WindNoiseGenerator as wng

import matplotlib.pyplot as plt
import time

# Parameters
DURATION = 12 # Duration in seconds
FS = 48000 # Sample frequency in Hz
GUSTINESS = 8 # Number of speed points. One yields constant wind. High values yield gusty wind (more than 10 can sound unnatural).
# WIND_PROFILE_OUTDOOR = np.array([3.45, 6.74, 5.65, 6.34, 4.00,
#                                  5.88, 3.26, 3.19, 4.78, 4.16,
#                                  4.67, 4.69, 4.61, 6.53, 6.05]) # Wind speed data example

WIND_PROFILE_OUTDOOR = np.array([5.05  , 8.05 , 1.45, 6.05, 5.05  , 8.05 , 10.05 , 8.05 , 1.45, 4.32]) # Wind speed data example
SEED = 1 # Seed for random sequence regeneration

# Generate wind noise
wn = wng(fs=FS, duration=DURATION, generate=True,
                wind_profile=WIND_PROFILE_OUTDOOR,
                gustiness=GUSTINESS,
                short_term_var=True, start_seed=SEED)
wn_signal, wind_profile = wn.generate_wind_noise()

# # Save signal in .wav file
# wn.save_signal(wn_signal, filename='./wind_noise_7.wav', num_ch=2, fs=16000)
# # Plot signal
# wn.plot_signals(wn_signal, wind_profile ,filename='./wind_noise_7.png' )

# print('debug 1')
# wn_signal, wind_profile = wn.generate_wind_noise()

# Save signal in .wav file
wn.save_signal(wn_signal, filename='./wind_noise_10.wav', num_ch=2, fs=48000)
# Plot signal
wn.plot_signals(wn_signal, wind_profile ,filename='./wind_noise_10.png' )

print('debug 2')


wn.play_signal(wn_signal)