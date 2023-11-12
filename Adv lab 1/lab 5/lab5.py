import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.fft import rfft, rfftfreq
from scipy.signal import find_peaks

#Change path for the 2 different sets of data
#path = "https://raw.githubusercontent.com/cchan011/Adv-lab/main/Adv%20lab%201/lab%205/lab5data1.csv" 
#uncomment above for data 1
path = "https://raw.githubusercontent.com/cchan011/Adv-lab/main/Adv%20lab%201/lab%205/lab5data2.csv" 
#uncomment above for data 2
data = np.genfromtxt(path, delimiter=",", names=True)

millisec = data["Time"]
A0 = data["Voltage"] 
time = millisec/1000
Voltage = np.divide(A0, 1023) * 5

yf = fft(A0)
xf = fftfreq(len(A0), 1/1000)

#peaks, _ = find_peaks(np.abs(yf), height = 5e4)
#peak_list = []
#peak_list_y = []
#i = 0
#while i <= 4:
#    j = round(float(xf[peaks[i]]), 4)
#    k = yf[peaks[i]]
#    peak_list.append(j)
#    peak_list_y.append(k)
#    i += 1

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize = (16,9))
ax1.set_xlim(0,0.2)
ax1.set_ylim(0,5)
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Voltage (V)')
ax1.set_title('Voltage vs Time graph')
ax1.plot(time, Voltage)
ax2.plot(xf, np.abs(yf),color='blue')
#ax2.plot(peak_list, np.abs(peak_list_y), 'x', color = "r")
ax2.set_xlabel('Frequency (Hz)')
ax2.set_ylabel('')
ax2.set_title('Signal graph')
ax2.set_xlim(0,600)
ax2.set_ylim(0,4e5)
ax2.grid()
#for a, b in enumerate(peak_list):
#    ax2.annotate(str(b)+'Hz', (peak_list[a] - 0.5, np.abs(peak_list_y[a]) + 7000))
plt.show()