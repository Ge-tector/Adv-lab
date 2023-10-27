import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.fft import rfft, rfftfreq
from scipy.signal import find_peaks

path = "https://raw.githubusercontent.com/cchan011/Adv-lab/main/Adv%20lab%201/lab%204/lab%204%20data.csv"
data = np.genfromtxt(path, delimiter=",", names=True)

millisec = data["Time"]
A0 = data["Output"] 

yf = fft(A0)
xf = fftfreq(len(A0), 1/1000)

peaks, _ = find_peaks(np.abs(yf), height = 5e4)
peak_list = []
peak_list_y = []
i = 0
while i <= 4:
    j = round(float(xf[peaks[i]]), 4)
    k = yf[peaks[i]]
    peak_list.append(j)
    peak_list_y.append(k)
    i += 1

fig, ax = plt.subplots()
ax.plot(xf, np.abs(yf),color='blue')
ax.plot(peak_list, np.abs(peak_list_y), 'x', color = "r")
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('')
ax.set_title('Signal graph')
ax.set_xlim(0,11)
ax.set_ylim(0,4e5)
ax.grid()
for a, b in enumerate(peak_list):
    ax.annotate(str(b)+'Hz', (peak_list[a] - 0.5, np.abs(peak_list_y[a]) + 7000))
plt.show()