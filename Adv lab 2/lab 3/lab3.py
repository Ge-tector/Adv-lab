import numpy as np
import matplotlib.pyplot as plt

exp3link = "https://raw.githubusercontent.com/cchan011/Adv-lab/main/Adv%20lab%202/lab%203/jeffexp3_trimmedData.csv"
exp4flink = "https://raw.githubusercontent.com/cchan011/Adv-lab/main/Adv%20lab%202/lab%203/jeffexp4-forward_trimmedData.csv"
exp4blink = "https://raw.githubusercontent.com/cchan011/Adv-lab/main/Adv%20lab%202/lab%203/jeffexp4-backwards_trimmedData.csv"
exp4rlink = "https://raw.githubusercontent.com/cchan011/Adv-lab/main/Adv%20lab%202/lab%203/jeffexp4-release_trimmedData.csv"

exp3 = np.genfromtxt(exp3link, delimiter=',', names=['Time','Angle1','Angle2'])
exp4f = np.genfromtxt(exp4flink, delimiter=',', names=['Time','Angle1','Angle2'])
exp4r = np.genfromtxt(exp4rlink, delimiter=',', names=['Time','Angle1','Angle2'])
exp4b = np.genfromtxt(exp4blink, delimiter=',', names=['Time','Angle1','Angle2'])

fig = plt.figure(0)
ax = plt.subplot()
ax.plot(exp3['Time'], exp3['Angle1'], color = 'blue', label = 'Horizontal Angle')
ax.plot(exp3['Time'], exp3['Angle2'], color = 'red', label = 'Vertical Angle')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Angle (rad)')
ax.set_title('Angle vs time graph under precession motion')
fig.legend(loc=2)

fig1 = plt.figure(1)
ax = plt.subplot()
ax.plot(exp4r['Time'], exp4r['Angle1'], color = 'blue', label = 'Horizontal Angle')
ax.plot(exp4r['Time'], exp4r['Angle2'], color = 'red', label = 'Vertical Angle')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Angle (rad)')
ax.set_title('Nutation graph, release with no momentum')
fig1.legend(loc=2)

fig2 = plt.figure(2)
ax = plt.subplot()
ax.plot(exp4f['Time'], exp4f['Angle1'], color = 'blue', label = 'Horizontal Angle')
ax.plot(exp4f['Time'], exp4f['Angle2'], color = 'red', label = 'Vertical Angle')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Angle (rad)')
ax.set_title('Nutation graph, release with forward momentum')
fig2.legend(loc=2)

fig3 = plt.figure(3)
ax = plt.subplot()
ax.plot(exp4b['Time'], exp4b['Angle1'], color = 'blue', label = 'Horizontal Angle')
ax.plot(exp4b['Time'], exp4b['Angle2'], color = 'red', label = 'Vertical Angle')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Angle (rad)')
ax.set_title('Nutation graph, release with backwards momentum')
fig3.legend(loc=2)

plt.show()