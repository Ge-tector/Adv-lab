import numpy as np
import matplotlib.pyplot as plt

#exp 2 n_i plot
#i feel like the pressure plot doesnt really matter (bc how N would change based on air property)
#N v n is more interesting

N_data = [1,3,8,10,14]
N = np.linspace(start=0, stop=100, num=101)

lambda_naught = 632.8e-9
lambda_avg = 621e-9
d = 2e-2

lambda_ratio = lambda_naught/lambda_avg

slope = -(lambda_naught/(2*d))

n_i_data = [(i * slope)+lambda_ratio for i in N_data]  
n_i_theoretical = [(i * slope)+lambda_ratio for i in N]

fig = plt.figure()
ax = plt.subplot()
ax.scatter(N_data, n_i_data, color = 'blue')
ax.plot(N, n_i_theoretical, color = 'black')
ax.set_title('N vs index of refraction graph')
ax.set_xlabel('N')
ax.set_ylabel('Index of refraction (n)')

plt.show()