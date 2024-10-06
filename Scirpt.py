import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Function to load seismic data
def load_seismic_data(file_path):
    # Assuming the file is in CSV format with 'time' and 'amplitude' columns
    data = pd.read_csv(file_path)
    return data['time'], data['amplitude']

# Function to analyze seismic activity
def analyze_seismic_activity(time, amplitude, threshold=0.5, distance=10):
    # Normalize amplitude
    normalized_amplitude = amplitude / np.max(np.abs(amplitude))

    # Find peaks in the amplitude data
    peaks, _ = find_peaks(normalized_amplitude, height=threshold, distance=distance)

    return peaks, normalized_amplitude

# Function to visualize results
def visualize_seismic_activity(time, amplitude, peaks):
    plt.figure(figsize=(12, 6))
    plt.plot(time, amplitude, label='Seismic Data', alpha=0.5)
    plt.plot(time[peaks], amplitude[peaks], "x", label='Detected Peaks', color='red')
    plt.title('Seismic Activity Analysis')
    plt.xlabel('Time (s)')
    plt.ylabel('Normalized Amplitude')
    plt.legend()
    plt.grid()
    plt.show()

# Main function to run the analysis
def main(apollo_file, mars_file):
    # Load Apollo data
    apollo_time, apollo_amplitude = load_seismic_data(apollo_file)
    apollo_peaks, apollo_normalized = analyze_seismic_activity(apollo_time, apollo_amplitude)
    visualize_seismic_activity(apollo_time, apollo_normalized, apollo_peaks)

    # Load Mars InSight data
    mars_time, mars_amplitude = load_seismic_data(mars_file)
    mars_peaks, mars_normalized = analyze_seismic_activity(mars_time, mars_amplitude)
    visualize_seismic_activity(mars_time, mars_normalized, mars_peaks)

if __name__ == "__main__":
    apollo_file = 'sample_signal.csv'  # Path to Apollo data
    mars_file = 'sample_signal1.csv'  # Path to Mars InSight data
    main(apollo_file, mars_file)
