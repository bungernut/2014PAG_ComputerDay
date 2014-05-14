import numpy

Nsims = 500000
nroll = lambda n,d: sum([int(numpy.ceil(numpy.random.rand()*d)) for i in range(n)])

r3d8 = numpy.zeros(25)
r4d6 = numpy.zeros(25)
r8d3 = numpy.zeros(25)
for i in range(Nsims):
    r3d8[nroll(3,8)]+=1
    r4d6[nroll(4,6)]+=1
    r8d3[nroll(8,3)]+=1

import matplotlib.pyplot as plt

plt.step(numpy.arange(25),r3d8/float(Nsims),color=(.6,.0,.6),label='3d8')
plt.step(numpy.arange(25),r4d6/float(Nsims),color=(0.1,.8,.1),label='4d6')
plt.step(numpy.arange(25),r8d3/float(Nsims),color=(0.1,.1,.9),label='8d3')
plt.legend()
plt.xlabel('Roll (sum)')
plt.ylabel('Probability')
plt.grid()
plt.savefig('dice_dnd.png')
