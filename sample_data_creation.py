import numpy as np
import pandas as pd

# Parameters for the signal
duration = 1.0  # seconds
sampling_rate = 1000  # samples per second
frequency = 5  # frequency of the sine wave in Hz
noise_amplitude = 0.5  # amplitude of the noise

# Generate time values
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Generate the signal (sine wave + noise)
signal = np.sin(2 * np.pi * frequency * t) + np.random.normal(0, noise_amplitude, size=t.shape)

# Create a DataFrame
data = pd.DataFrame({'time': t, 'amplitude': signal})

# Save to CSV
data.to_csv('sample_signal1.csv', index=False)
