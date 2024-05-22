import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import poisson
from scipy.stats import norm
from scipy.stats import linregress

file = pd.read_excel(r"C:\Users\cp4c5\OneDrive\文件\GitHub\Adv-lab\final\Chan3967522804.xls")
#problem 1. to use, uncomment this block and comment the problem 2 block.
'''
A = file["A"]
A.pop(0)

fig = plt.figure(0)
ax = plt.subplot()
ax.hist(A[1:2001], density = True, bins = [0,1,2,3,4,5], label = 'Data')
ax.set_xticks(range(6))
#ax.plot([0,1,2,3,4,5], poisson.pmf([0,1,2,3,4,5], 1 , loc=1), label = 'Ideal')
ax.plot([0,1,2,3,4,5], norm.pdf([0,1,2,3,4,5], 1.42), label = 'Ideal')
ax.set_title('Normalized histogram for data set A')
fig.legend(loc=2)

B = file["B"]
B.pop(0)

fig1 = plt.figure(1)
ax1 = plt.subplot()
ax1.hist(B[1:2001], density = True, bins = [0,1,2,3,4,5,6,7], label = 'Data')
ax1.set_xticks(range(8))
ax1.plot([0,1,2,3,4,5,6,7], poisson.pmf([0,1,2,3,4,5,6,7], 0.99 , loc=0), label = 'Ideal')
ax1.set_title('Normalized histogram for data set B')
fig1.legend(loc=2)

C = file["C"]
C.pop(0)

fig2 = plt.figure(2)
ax2 = plt.subplot()
ax2.hist(C, density = True, bins = 100, label = 'Data')
idealizedC = np.arange(-180, 0, 0.001)
ax2.plot(idealizedC, norm.pdf(idealizedC, -86.5212,25), label = 'Ideal')
ax2.set_title('Normalized histogram for data set C')
fig2.legend(loc=2)
'''

#problem 2. to use, make sure to comment out first block.

Qx = file['Qx']
Qx.pop(0)
Qy = file['Qy']
Qy.pop(0)
Rx = file['Rx']
Rx.pop(0)
Ry = file['Ry']
Ry.pop(0)
'''
#linear x linear y
fig = plt.figure(0)
linear = plt.subplot()
linear.plot(Qx, Qy, 'o', color = 'blue', label = 'Data') #this line doesnt have the log(~0) problem
#linear.plot(Rx, Ry, color = 'red')
linear.set_title('Linear X and Linear Y')
linear.set_xlabel('Qx')
linear.set_ylabel('Qy')

QLinRegress = linregress(Qx[1:6], Qy[1:6])
linear.plot(Qx, QLinRegress.intercept + QLinRegress.slope*Qx, color = 'red', label = 'Fitted Line')

print('The following values are for the Q dataset.')
print('Slope of Best Fit: ' + str(QLinRegress.slope))
print('Y-intercept of Best Fit: ' + str(QLinRegress.intercept))

x = 1
N = 6 
Yuncertainty = 0
while x < N:
    Yuncertainty += np.sqrt(1/(N-2))*np.sqrt((Qy[x]-QLinRegress.intercept-QLinRegress.slope*Qx[x])**2) #formula from textbook
    x += 1

print('Uncertainty of Y: '+str(Yuncertainty))
print('Uncertainty of slope: '+str(QLinRegress.stderr))
print('Uncertainty of Y intercept: '+str(QLinRegress.intercept_stderr))
print('Linear Correlation coefficient R: '+str(QLinRegress.rvalue))

linear.plot(Qx, QLinRegress.intercept + Yuncertainty + QLinRegress.slope*Qx, linestyle = 'dashed', color = 'red')
linear.plot(Qx, QLinRegress.intercept - Yuncertainty + QLinRegress.slope*Qx, linestyle = 'dashed', color = 'red')

fig.legend(loc=2)
'''

#linear x and log y
fig1 = plt.figure(1)
linlog = plt.subplot()
logRy = np.log(Ry[0:29])
#linlog.plot(Qx, np.log(Qy), color = 'blue') #numbers close to zero blows way up
linlog.plot(Rx[0:29], logRy, 'o', color = 'blue', label = 'Data') #most straightline like for this one
linlog.set_title('Linear X and Log Y')
linlog.set_xlabel('Rx')
linlog.set_ylabel('Ry')

RLinRegress = linregress(Rx[0:29], logRy)
linlog.plot(Rx, RLinRegress.intercept + RLinRegress.slope*Rx, color = 'red', label = 'Fitted Line')

print('The following values are for the R dataset.')
print('Slope of Best Fit: ' + str(RLinRegress.slope))
print('Y-intercept of Best Fit: ' + str(RLinRegress.intercept))

x = 1
N = 29 
Yuncertainty = 0
while x < N:
    Yuncertainty += np.sqrt(1/(N-2))*np.sqrt((logRy[x]-RLinRegress.intercept-RLinRegress.slope*Rx[x])**2) #formula from textbook
    x += 1

print('Uncertainty of Y: '+str(Yuncertainty))
print('Uncertainty of slope: '+str(RLinRegress.stderr))
print('Uncertainty of Y intercept: '+str(RLinRegress.intercept_stderr))
print('Linear Correlation coefficient R: '+str(RLinRegress.rvalue))

linlog.plot(Rx, RLinRegress.intercept + Yuncertainty + RLinRegress.slope*Rx, linestyle = 'dashed', color = 'red')
linlog.plot(Rx, RLinRegress.intercept - Yuncertainty + RLinRegress.slope*Rx, linestyle = 'dashed', color = 'red')

fig1.legend(loc=2)



'''
#log x linear y
fig2 = plt.figure(2)
loglin = plt.subplot()
loglin.plot(np.log(Qx), Qy, color = 'blue')
#loglin.plot(np.log(Rx), Ry, color = 'red')
loglin.set_title('loglin')

#log x log y
fig3 = plt.figure(3)
loglog = plt.subplot()
loglog.plot(np.log(Qx), np.log(Qy), color = 'blue')
#loglog.plot(np.log(Rx), np.log(Ry), color = 'red')
loglog.set_title('loglog')
'''

plt.show()