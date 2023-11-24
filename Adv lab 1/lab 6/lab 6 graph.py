import numpy as np
import matplotlib.pyplot as plt

#While I could consolidate all the data recording into 1 file, I am lazy and did not want to copy and paste all datas one by one. So I will copy and paste different paths one by one instead.
path = "https://raw.githubusercontent.com/cchan011/Adv-lab/main/Adv%20lab%201/lab%206/lab%206%20ir%20no%20glass.csv" 
data = np.genfromtxt(path, delimiter=",", names=True) 
irng = np.mean(data["Voltage"]) #infrared, no glass

path = "https://raw.githubusercontent.com/cchan011/Adv-lab/main/Adv%20lab%201/lab%206/lab%206%20ir%20glass.csv" 
data = np.genfromtxt(path, delimiter=",", names=True) 
irg = np.mean(data["Voltage"]) #infrared, glass

path = "https://raw.githubusercontent.com/cchan011/Adv-lab/main/Adv%20lab%201/lab%206/lab%206%20red%20no%20glass.csv" 
data = np.genfromtxt(path, delimiter=",", names=True) 
rng = np.mean(data["Voltage"]) #red, no glass

path = "https://raw.githubusercontent.com/cchan011/Adv-lab/main/Adv%20lab%201/lab%206/lab%206%20red%20glass.csv" 
data = np.genfromtxt(path, delimiter=",", names=True)
rg = np.mean(data["Voltage"]) #red, glass

path = "https://raw.githubusercontent.com/cchan011/Adv-lab/main/Adv%20lab%201/lab%206/lab%206%20yellow%20no%20glass.csv" 
data = np.genfromtxt(path, delimiter=",", names=True)
yng = np.mean(data["Voltage"]) #yellow, no glass

path = "https://raw.githubusercontent.com/cchan011/Adv-lab/main/Adv%20lab%201/lab%206/lab%206%20yellow%20glass.csv" 
data = np.genfromtxt(path, delimiter=",", names=True)
yg = np.mean(data["Voltage"]) #yellow, glass

path = "https://raw.githubusercontent.com/cchan011/Adv-lab/main/Adv%20lab%201/lab%206/lab%206%20green%20no%20glass.csv" 
data = np.genfromtxt(path, delimiter=",", names=True)
gng = np.mean(data["Voltage"]) #green, no glass

path = "https://raw.githubusercontent.com/cchan011/Adv-lab/main/Adv%20lab%201/lab%206/lab%206%20green%20glass.csv" 
data = np.genfromtxt(path, delimiter=",", names=True)
gg = np.mean(data["Voltage"]) #green, glass

path = "https://raw.githubusercontent.com/cchan011/Adv-lab/main/Adv%20lab%201/lab%206/lab%206%20uv%20no%20glass.csv" 
data = np.genfromtxt(path, delimiter=",", names=True)
uvng = np.mean(data["Voltage"]) #uv, no glass

path = "https://raw.githubusercontent.com/cchan011/Adv-lab/main/Adv%20lab%201/lab%206/lab%206%20uv%20glass.csv" 
data = np.genfromtxt(path, delimiter=",", names=True)
uvg = np.mean(data["Voltage"])  #uv, glass

#percentage calculation
ir = (irg/irng)*100
r = (rg/rng)*100
y = (yg/yng)*100
g = (gg/gng)*100
uv = (uvg/uvng)*100
percentage = np.around([uv, g, y, r, ir], decimals = 1)

#wavelength list
wavelength = [490, 569, 587, 625, 940]

fig, ax = plt.subplots()
ax.set_xlim([450, 1000])
ax.set_ylim([0, 100])
ax.set_xlabel('Wavelength (nm)')
ax.set_ylabel('Transmission percentage (%)')
ax.set_title('Transmission percentage graph')

#color code/style
style = ['xb', 'xg', 'xy', 'xr', 'xk']
colorList = ['blue', 'green', 'gold', 'red', 'black']
text = ['UV', 'Green', 'Yellow', 'Red', 'IR']

for a, b in enumerate(percentage):
    ax.plot(wavelength[a], percentage[a], style[a])
    ax.annotate(text[a] + ':' + ' ' + str(b)+'%', (wavelength[a] - 30, b+3), color = colorList[a])

plt.show()

