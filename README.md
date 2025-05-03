# LC Resonance Circuit – LTSpice Simulation & Python Visualization

This project simulates an **LC resonance circuit** with variable damping resistance using **LTSpice**, and visualizes the output using **Python (Matplotlib)**. It is part of my coursework in *Bauelemente und Schaltungstechnik* at Universität Siegen and contributes to my analog/mixed-signal skill development.

---

## 🔧 Project Overview

We analyze a simple RLC series circuit with:

- **L** = 20 mH  
- **C** = 10 nF  
- **R2** = [20 Ω, 80 Ω, 200 Ω]  
- **AC Source** = 1V small signal sweep

The goal is to examine:

- Resonant frequency  
- Output voltage amplitude  
- Bandwidth and quality factor (Q)  
- Impact of resistance on selectivity and damping

---

## 🧪 LTSpice Simulation

The AC sweep is performed across different R values. Data is exported using LTSpice's waveform viewer as a `.txt` file for external processing.

📁 Files:
- `Aufgabe_LC_Resonance/RLC.asc` – Circuit schematic  
- `Aufgabe_LC_Resonance/report.pdf` – Detailed write-up  
- `Aufgabe_LC_Resonance/rlc_response.txt` – Exported frequency-voltage data  

---

## 📊 Python Visualization

The exported LTSpice data was processed using a custom Python script with `matplotlib`. Voltage values were extracted from the dB-formatted string and converted to linear mV scale.

📁 Files:
- `plot_rlc_response.py` – Script to parse and plot the data  
- `rlc_response_plot.png` – Output frequency response graph

📉 Preview:

![LTSpice Plot](Aufgabe_LC_Resonance/rlc_response_plot.png)

---

## 📁 Folder Structure

```plaintext
LC-Resonance-Circuit-ltspice/
├── README.md
└── Aufgabe_LC_Resonance/
    ├── RLC.asc                  ← LTSpice schematic
    ├── report.pdf               ← Full assignment report
    ├── rlc_response.txt         ← Exported simulation data
    ├── plot_rlc_response.py     ← Python script for plotting
    └── rlc_response_plot.png    ← Resulting frequency response plot
---

## 👨‍🎓 Author

**Mainak Roy**  
🎓 M.Sc. Electrical Engineering – Electronics Design & Technology  
🏫 Universität Siegen  

🌐 GitHub: [@238Roy](https://github.com/238Roy) Contact: mainak.roy@student.uni-siegen.de
   

