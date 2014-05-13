import numpy
import math
# Setup MCA (DAQ)
chns = 1024              # chanels in MCA
energy_scale = 80.       #chn/MeV
energy_offset = 0.1      #MeV @ chn=1

# Diode properties
h = 0.56 #um
dEdX = 0.11 #MeV/um
gauss_sigma = 0.009 #MeV

def diode_out(alpha_energy):
    # Choose a random direction for the alpha
    # particle in spherical coordinates
    theta = numpy.random.random() # 2*pi
    if theta >= 0.5:
      #skip it, alpha went the wrong way
      return 0
    phi = math.acos(2.*numpy.random.random() - 1.)
    
    #The length the track is in the silicone
    L = alpha_energy/dEdX
    
    # the dead layer wont make detectable energy
    L_dead = h/math.sin(phi)
    
    #Energy remaining to deposit in active layer
    E_dep = (L-L_dead)*dEdX
    
    # Smear the energy deposit by gaussian energy resolution
    E_dep_smear = numpy.random.normal(E_dep,gauss_sigma,1)[0]
    return int(math.floor((energy_offset+E_dep_smear)*80.))

# Lets simulate some events!
N = 100000
alpha_e = 6.0 # MeV
MCA_buffer = numpy.zeros(chns)
for i in range(N):
    bin = diode_out(alpha_e)
    MCA_buffer[bin]+=1


import matplotlib.pyplot as plt
plt.step(numpy.arange(chns),MCA_buffer/float(N))
plt.plot(0,MCA_buffer[0]/float(N),'rx')
plt.title('Simulation of Alpha=%.2f MeV (N=%d)'%(alpha_e,N))
plt.xlabel('MCA Channel')
plt.ylabel('PDF')
plt.xlim((0,chns))
plt.savefig('diode_sim_pdf.png')
plt.close('all')
