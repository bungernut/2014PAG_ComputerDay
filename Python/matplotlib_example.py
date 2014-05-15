import matplotlib
#If running on scinence uncomment this line
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy

x = numpy.arange(1000)
y1 = 50*numpy.exp(-x/100.)
y2 = 10*(1-numpy.exp(-x/1000.))
noise = numpy.random.rand(x.size)

fig = plt.figure(figsize=(9,6))
plt.plot(x,y1+y2+noise,label='dbl exp')
plt.xlabel('time')
plt.ylabel('Counts')
plt.savefig('matplot.png')
