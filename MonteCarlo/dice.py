import numpy

roll = lambda n: int(numpy.ceil(numpy.random.rand()*n))
Nsims = 500000

r3d8 = numpy.zeros(25)
r4d6 = numpy.zeros(25)
r8d3 = numpy.zeros(25)
for i in range(Nsims):
    r3d8[sum([roll(8),roll(8),roll(8)])]+=1
    r4d6[sum([roll(6),roll(6),roll(6),roll(6)])]+=1
    r8d3[sum([roll(3),roll(3),roll(3),roll(3),roll(3),roll(3),roll(3),roll(3)])]+=1

import matplotlib.pyplot as plt

plt.step(numpy.arange(25),r3d8/float(Nsims),color=(.6,.0,.6),label='3d8')
plt.step(numpy.arange(25),r4d6/float(Nsims),color=(0.1,.8,.1),label='4d6')
plt.step(numpy.arange(25),r8d3/float(Nsims),color=(0.1,.1,.9),label='8d3')
plt.legend()
plt.xlabel('Roll (sum)')
plt.ylabel('Probability')
plt.grid()
plt.savefig('dice_dnd.png')
