import numpy as np
import matplotlib.pyplot as plt
from choke_match import *
from classic_match import *


#runs the choke_match simulation and graphs the results.

x = np.linspace(.4,.6,50)

plt.plot(x,run_sim_range_classic(.4,.6,3000), label = 'standard')
plt.plot(x,run_sim_range_choke(.45,.4,.6,3000), label = 'pc =.45')
plt.plot(x,run_sim_range_choke(.4,.4,.6,3000), label ='pc =.4')
plt.plot(x,run_sim_range_choke(.35,.4,.6, 3000), label = 'pc =.35')
plt.plot(x,run_sim_range_choke(.3,.4,.6, 3000), label = 'pc =.3')
plt.plot(x,run_sim_range_choke(.25,.4,.6, 3000), label = 'pc =.25')

plt.legend()
plt.xlabel('probability of winning a given point')
plt.ylabel('probability of winning match')
plt.show()
