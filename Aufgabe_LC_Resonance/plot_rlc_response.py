import numpy as np
import matplotlib.pyplot as plt
import re

# === File path to your LTSpice export ===
file_path = r'C:\Users\royma\Documents\LTSpice\rlc_response.txt'  # Update path if needed

# === Read the data ===
frequencies = []
voltages_db = []

with open(file_path, 'r') as file:
    for line in file:
        if 'Step' in line or 'Freq.' in line or line.strip() == '':
            continue  # skip headers and step info
        
        parts = line.strip().split('\t')
        if len(parts) < 2:
            continue
        
        freq = float(parts[0])
        
        # Extract dB from the voltage format like (-4.623e+01dB, -87°)
        db_match = re.search(r'\((-?[\d\.e\+\-]+)dB', parts[1])
        if db_match:
            v_db = float(db_match.group(1))
            frequencies.append(freq)
            voltages_db.append(v_db)

# === Convert to numpy arrays ===
frequencies = np.array(frequencies)
voltages_db = np.array(voltages_db)

# === Convert dB to linear scale (V), then to mV ===
voltages_mv = 10 ** (voltages_db / 20) * 1000  # from dB to V, then to mV

# === Plot ===
plt.figure(figsize=(10, 6))
plt.plot(frequencies / 1000, voltages_mv, color='blue', label='V(out) [from LTSpice]')
plt.title('LTSpice RLC Response – Frequency vs Output Voltage')
plt.xlabel('Frequency (kHz)')
plt.ylabel('Output Voltage (mV)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("rlc_response_plot.png")
plt.show()
