import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
csv_file = 'sample_signal.csv'  # Replace with your CSV file path
data = pd.read_csv(csv_file)

# Assume the relevant columns are 'time' and 'amplitude'
time = data['time'].values
amplitude = data['amplitude'].values

# Compute FFT using NumPy
fft_result = np.fft.fft(amplitude)

# Sampling interval
T = time[1] - time[0]  # Assuming uniform sampling
N = len(amplitude)
freq = np.fft.fftfreq(N, T)

# Plotting
plt.subplot(2, 1, 1)
plt.plot(time, amplitude)
plt.title('Original Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(freq[:N // 2], np.abs(fft_result)[:N // 2])  # Only plot positive frequencies
plt.title('FFT of the Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')

plt.tight_layout()
plt.show()
