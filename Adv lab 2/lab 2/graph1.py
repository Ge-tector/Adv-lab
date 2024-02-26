import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from numpy import diff

apath0 = "https://raw.githubusercontent.com/cchan011/Adv-lab/main/Adv%20lab%202/lab%202/Lab2Data_Jeff/jeff/aluminumtest1.csv"
apath1 = "https://raw.githubusercontent.com/cchan011/Adv-lab/main/Adv%20lab%202/lab%202/Lab2Data_Jeff/jeff/aluminumtest2.csv"
apath2 = "https://raw.githubusercontent.com/cchan011/Adv-lab/main/Adv%20lab%202/lab%202/Lab2Data_Jeff/jeff/aluminumtest3.csv"
apath3 = "https://raw.githubusercontent.com/cchan011/Adv-lab/main/Adv%20lab%202/lab%202/Lab2Data_Jeff/jeff/aluminumtest4.csv"
apath4 = "https://raw.githubusercontent.com/cchan011/Adv-lab/main/Adv%20lab%202/lab%202/Lab2Data_Jeff/jeff/aluminumtest5.csv"

cpath0 = "https://raw.githubusercontent.com/cchan011/Adv-lab/main/Adv%20lab%202/lab%202/Lab2Data_Jeff/jeff/coppertest1.csv"
cpath1 = "https://raw.githubusercontent.com/cchan011/Adv-lab/main/Adv%20lab%202/lab%202/Lab2Data_Jeff/jeff/coppertest2.csv"
cpath2 = "https://raw.githubusercontent.com/cchan011/Adv-lab/main/Adv%20lab%202/lab%202/Lab2Data_Jeff/jeff/coppertest3.csv"
cpath3 = "https://raw.githubusercontent.com/cchan011/Adv-lab/main/Adv%20lab%202/lab%202/Lab2Data_Jeff/jeff/coppertest4.csv"
cpath4 = "https://raw.githubusercontent.com/cchan011/Adv-lab/main/Adv%20lab%202/lab%202/Lab2Data_Jeff/jeff/coppertest5.csv"


adata0 = np.genfromtxt(apath0, delimiter=',', usecols=(3,4,10),names=['time','ch1','ch2'])
adata1 = np.genfromtxt(apath1, delimiter=',', usecols=(3,4,10),names=['time','ch1','ch2'])
adata2 = np.genfromtxt(apath2, delimiter=',', usecols=(3,4,10),names=['time','ch1','ch2'])
adata3 = np.genfromtxt(apath3, delimiter=',', usecols=(3,4,10),names=['time','ch1','ch2'])
adata4 = np.genfromtxt(apath4, delimiter=',', usecols=(3,4,10),names=['time','ch1','ch2'])

cdata0 = np.genfromtxt(cpath0, delimiter=',', usecols=(3,4,10),names=['time','ch1','ch2'])
cdata1 = np.genfromtxt(cpath1, delimiter=',', usecols=(3,4,10),names=['time','ch1','ch2'])
cdata2 = np.genfromtxt(cpath2, delimiter=',', usecols=(3,4,10),names=['time','ch1','ch2'])
cdata3 = np.genfromtxt(cpath3, delimiter=',', usecols=(3,4,10),names=['time','ch1','ch2'])
cdata4 = np.genfromtxt(cpath4, delimiter=',', usecols=(3,4,10),names=['time','ch1','ch2'])


fig = plt.figure(figsize=([16, 9]))
gs = gridspec.GridSpec(2, 6)
gs.update(wspace = 1.5, hspace = 0.3)

time = adata0['time']*1000
ch1data = adata0['ch1']
ch2data = adata0['ch2']
ax1 = plt.subplot(gs[0, :2])
ax2 = ax1.twinx()
ax1.plot(time, ch1data, color='steelblue',label='Ch1')
ax1.set_xlabel('Time (ms)')
ax1.set_ylabel('Voltage (V)')
ax1.set_title('Aluminum rod data 1 graph')
ax1.grid()
ax2.plot(time, ch2data, color='red',label='Ch2')
ax1.tick_params(axis='y',colors='steelblue')
ax2.tick_params(axis='y',colors='red')

time = adata1['time']*1000
ch1data = adata1['ch1']
ch2data = adata1['ch2']
ax3 = plt.subplot(gs[0, 2:4])
ax4 = ax3.twinx()
ax3.plot(time, ch1data, color='steelblue')
ax3.set_xlabel('Time (ms)')
ax3.set_ylabel('Voltage (V)')
ax3.set_title('Aluminum rod data 2 graph')
ax3.grid()
ax4.plot(time, ch2data, color='red')
ax3.tick_params(axis='y',colors='steelblue')
ax4.tick_params(axis='y',colors='red')


time = adata2['time']*1000
ch1data = adata2['ch1']
ch2data = adata2['ch2']
ax5 = plt.subplot(gs[0, 4:6])
ax6 = ax5.twinx()
ax5.plot(time, ch1data, color='steelblue')
ax5.set_xlabel('Time (ms)')
ax5.set_ylabel('Voltage (V)')
ax5.set_title('Aluminum rod data 3 graph')
ax5.grid()
ax6.plot(time, ch2data, color='red')
ax5.tick_params(axis='y',colors='steelblue')
ax6.tick_params(axis='y',colors='red')


time = adata3['time']*1000
ch1data = adata3['ch1']
ch2data = adata3['ch2']
ax7 = plt.subplot(gs[1, 1:3])
ax8 = ax7.twinx()
ax7.plot(time, ch1data, color='steelblue')
ax7.set_xlabel('Time (ms)')
ax7.set_ylabel('Voltage (V)')
ax7.set_title('Aluminum rod data 4 graph')
ax7.grid()
ax8.plot(time, ch2data, color='red')
ax7.tick_params(axis='y',colors='steelblue')
ax8.tick_params(axis='y',colors='red')


time = adata4['time']*1000
ch1data = adata4['ch1']
ch2data = adata4['ch2']
ax9 = plt.subplot(gs[1, 3:5])
ax10 = ax9.twinx()
ax9.plot(time, ch1data, color='steelblue')
ax9.set_xlabel('Time (ms)')
ax9.set_ylabel('Voltage (V)')
ax9.set_title('Aluminum rod data 5 graph')
ax9.grid()
ax10.plot(time, ch2data, color='red')
ax9.tick_params(axis='y',colors='steelblue')
ax10.tick_params(axis='y',colors='red')

fig.legend(loc = 2)

fig2 = plt.figure(figsize=([16, 9]))

time = cdata0['time']*1000
ch1data = cdata0['ch1']
ch2data = cdata0['ch2']
ax1 = plt.subplot(gs[0, :2])
ax2 = ax1.twinx()
ax1.plot(time, ch1data, color='steelblue',label='ch1')
ax1.set_xlabel('Time (ms)')
ax1.set_ylabel('Voltage (V)')
ax1.set_title('Copper rod data 1 graph')
ax1.grid()
ax2.plot(time, ch2data, color='red',label='ch2')
ax1.tick_params(axis='y',colors='steelblue')
ax2.tick_params(axis='y',colors='red')


time = cdata1['time']*1000
ch1data = cdata1['ch1']
ch2data = cdata1['ch2']
ax3 = plt.subplot(gs[0, 2:4])
ax4 = ax3.twinx()
ax3.plot(time, ch1data, color='steelblue')
ax3.set_xlabel('Time (ms)')
ax3.set_ylabel('Voltage (V)')
ax3.set_title('Copper rod data 2 graph')
ax3.grid()
ax4.plot(time, ch2data, color='red')
ax3.tick_params(axis='y',colors='steelblue')
ax4.tick_params(axis='y',colors='red')

time = cdata2['time']*1000
ch1data = cdata2['ch1']
ch2data = cdata2['ch2']
ax5 = plt.subplot(gs[0, 4:6])
ax6 = ax5.twinx()
ax5.plot(time, ch1data, color='steelblue')
ax5.set_xlabel('Time (ms)')
ax5.set_ylabel('Voltage (V)')
ax5.set_title('Copper rod data 3 graph')
ax5.grid()
ax6.plot(time, ch2data, color='red')
ax5.tick_params(axis='y',colors='steelblue')
ax6.tick_params(axis='y',colors='red')


time = cdata3['time']/1000
ch1data = cdata3['ch1']
ch2data = cdata3['ch2']
ax7 = plt.subplot(gs[1, 1:3])
ax8 = ax7.twinx()
ax7.plot(time, ch1data, color='steelblue')
ax7.set_xlabel('Time (ms)')
ax7.set_ylabel('Voltage (V)')
ax7.set_title('Copper rod data 4 graph')
ax7.grid()
ax8.plot(time, ch2data, color='red')
ax7.tick_params(axis='y',colors='steelblue')
ax8.tick_params(axis='y',colors='red')


time = cdata4['time']/1000
ch1data = cdata4['ch1']
ch2data = cdata4['ch2']
ax9 = plt.subplot(gs[1, 3:5])
ax10 = ax9.twinx()
ax9.plot(time, ch1data, color='steelblue')
ax9.set_xlabel('Time (ms)')
ax9.set_ylabel('Voltage (V)')
ax9.set_title('Copper rod data 5 graph')
ax9.grid()
ax10.plot(time, ch2data, color='red')
ax9.tick_params(axis='y',colors='steelblue')
ax10.tick_params(axis='y',colors='red')

fig2.legend(loc = 2)
'''
below is obtaining delta T using coding
the idea is to grab both ch2 jump (using normal math comparison) and ch1 ramp up using derivatives
'''
AluminumDeltaT = []
CopperDeltaT = []
adata = [adata0, adata1, adata2, adata3, adata4]
cdata = [cdata0, cdata1, cdata2, cdata3, cdata4]
ch2jump = float()
ch1ramp = float()
#print(adata0['ch2'][1])
a = 0
while a <= 4:
    x = 0
    currentdata = adata[a]
    ch2list = currentdata['ch2']
    while x < len(ch2list):
        if ch2list[x] > 0.5:
            timelist = currentdata['time']
            ch2jump = timelist[x]
            break
        else:
            x += 1
    dx = 0.00001
    dy = diff(currentdata['time'])/dx
    ch1list = currentdata['ch1']
    while x < len(dy):
        if dy[x] > 10:
            timelist = currentdata['time']
            ch1ramp = timelist[x] #the n-1 from numpy.diff doesnt matter bc we have large sample size and other than the actual increase, the other time spots dont matter
            break
        else:
            x += 1
    AluminumDeltaT.append((ch1ramp-ch2jump)*1000)
    #print(ch1ramp)
    #print(ch2jump)
    a += 1
b = 0
while b <= 4:
    x = 0
    currentdata = cdata[b]
    ch2list = currentdata['ch2']
    while x < len(ch2list):
        if ch2list[x] > 0.5:
            timelist = currentdata['time']
            ch2jump = timelist[x]
            break
        else:
            x += 1
    dx = 0.00001
    dy = diff(currentdata['time'])/dx
    ch1list = currentdata['ch1']
    while x < len(dy):
        if dy[x] > 10:
            timelist = currentdata['time']
            ch1ramp = timelist[x] #the n-1 from numpy.diff doesnt matter bc we have large sample size and other than the actual increase, the other time spots dont matter
            break
        else:
            x += 1
    CopperDeltaT.append((ch1ramp-ch2jump)*1000)
    b += 1

print('Aluminum average delta T = '+str(np.average(AluminumDeltaT))) #getting average time
print('Copper average delta T = '+str(np.average(CopperDeltaT)))

fig3 = plt.figure()
ax11 = plt.subplot()
ax12 = ax11.twinx()
ax11.scatter([1,2,3,4,5], AluminumDeltaT, color='steelblue', marker='o', label = 'Aluminum')
ax12.scatter([1,2,3,4,5], CopperDeltaT, color='red', marker='o', label = 'Copper')
ax11.set_ylabel('Time difference (ms)')
ax11.set_xlabel('Trial number')
ax11.set_title('Delta T calculated via coding for all 5 trials')
ax11.tick_params(axis='y',colors='steelblue')
ax12.tick_params(axis='y',colors='red')
plt.xticks([int(1),int(2),int(3),int(4),int(5)])
fig3.legend(loc = 2, bbox_to_anchor = (0,1), bbox_transform=ax11.transAxes)





plt.show()