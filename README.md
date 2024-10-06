

# WaveX

WaveX is a Python-based project designed to process and analyze wave data, particularly focusing on Fourier Transform techniques to extract frequency domain characteristics from time-domain signals. The project is equipped with scripts to simulate, process, and analyze waveforms and related data.

## Features

- **Fast Fourier Transform (FFT) Analysis**: Convert time-domain signals into the frequency domain using FFT to gain insights into frequency components.
- **Data Simulation**: Custom scripts to generate sample signals for analysis.
- **Seismic Wave Characteristics**: Tools to analyze seismic wave properties using signal processing techniques.

## Getting Started

### Prerequisites

Ensure you have the following libraries installed:

```bash
pip install numpy pandas matplotlib
```

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/WaveX.git
   cd WaveX
   ```

2. Place your signal data (CSV files) in the root directory or specify the file path in the script.

### Usage

#### FFT Analysis

The `fft.py` script performs Fourier Transform on a given signal stored in a CSV file. The signal should have two columns: `time` and `amplitude`.

To run the FFT analysis:

```bash
python fft.py
```

This will generate two plots:
1. **Original Signal**: Plot of amplitude vs. time.
2. **FFT of the Signal**: Magnitude vs. Frequency plot of the signal.

#### Data Simulation

The `sample_data_creation.py` script allows users to generate sample signal data for testing purposes.

```bash
python sample_data_creation.py
```

#### Seismic Wave Characteristics

Use the `seismic_wave_characterstics.py` script to analyze seismic wave signals for various properties.

```bash
python seismic_wave_characterstics.py
```

### Example

Here’s an example of how the FFT of a sample signal is visualized:

1. The original signal in the time domain.
2. The corresponding frequency domain representation after performing FFT.

### Folder Structure

```
WaveX/
│
├── fft.py                   # Script to perform FFT analysis
├── sample_data_creation.py   # Script to create sample data for testing
├── seismic_wave_characterstics.py # Script to analyze seismic wave properties
├── sample_signal.csv         # Sample signal data file (replace with your data)
└── README.md                 # Project documentation
```

### Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue to discuss what you would like to change.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

You can modify this as needed to fit your specific project details. Let me know if you want any specific updates!
