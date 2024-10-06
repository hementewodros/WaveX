import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, welch

# Step 1: Load the seismic data, skipping the header
data = np.genfromtxt('sample_signal.csv', delimiter=',', skip_header=1)
time = data[:, 0]
amplitude = data[:, 1]

# Step 2: Plot the seismic data
plt.figure(figsize=(10, 4))
plt.plot(time, amplitude)
plt.title('Seismic Data')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

# Step 3: Identify peaks in the amplitude data
peaks, properties = find_peaks(amplitude, height=0)  # Adjust height based on your data
print(f'Detected Peaks: {peaks}')

# Step 4: Plot the detected peaks
plt.figure(figsize=(10, 4))
plt.plot(time, amplitude)
plt.plot(time[peaks], amplitude[peaks], "x", label='Detected Peaks')
plt.title('Detected Peaks in Seismic Data')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()
plt.show()

# Step 5: Analyze the frequency content using Welch's method
fs = 100  # Sample frequency (Hz) - adjust based on your data
frequencies, psd = welch(amplitude, fs=fs, nperseg=1024)

# Step 6: Plot the Power Spectral Density (PSD)
plt.figure(figsize=(10, 4))
plt.semilogy(frequencies, psd)
plt.title('Power Spectral Density')
plt.xlabel('Frequency (Hz)')
plt.ylabel('PSD (V^2/Hz)')
plt.grid()
plt.show()

# Step 7: Compute Signal-to-Noise Ratio (SNR)
# Mean power of detected peaks
signal_power = np.mean(amplitude[peaks]**2)

# Mean power of the entire signal
total_power = np.mean(amplitude**2)

# Noise power calculation
noise_power = total_power - signal_power

# SNR calculation
snr = 10 * np.log10(signal_power / noise_power)
print(f'Signal-to-Noise Ratio (SNR): {snr:.2f} dB')
