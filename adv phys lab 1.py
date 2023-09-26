#adv phys lab 1
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
<<<<<<< Updated upstream
=======
ax.set_xlim([0, 8000]) #goes into negative before 8000 ohms
>>>>>>> Stashed changes
ax.set_ylim([0, 5])
ax.set_title(r'Relation between $V_{out}$ and $R_1$')
ax.set_xlabel(r"$R_1$ ($\Omega$)")
ax.set_ylabel(r"$V_{out}$ (V)")
<<<<<<< Updated upstream
R_1 = np.linspace(0, 30000,3000) #100 ohm per step
V_out = (5/(4644+R_1))*(4644)
=======
R_1 = np.linspace(0, 8000, 800) #100 ohm per step
V_out = 5 - (0.0006697*R_1)
>>>>>>> Stashed changes

ax.plot(R_1, V_out)
ax.plot(R_1[280], V_out[280], 'bo') #2822 is close to 2800
plt.annotate("Experimental result", 
             xy=(R_1[280], V_out[280]), 
<<<<<<< Updated upstream
             textcoords="offset points",xytext=(40,40), 
=======
             textcoords="offset points",xytext=(-40,-40), 
>>>>>>> Stashed changes
             ha='center',
             va='bottom',
             arrowprops=dict(arrowstyle = '-|>', connectionstyle='arc3, rad=0')) 

plt.show()
