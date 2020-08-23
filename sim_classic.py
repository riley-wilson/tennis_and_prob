import matplotlib.pyplot as plt
import numpy as np
from classic_match import *



def run_sim(p, n):

    results = []

    for i in range(n):
        m = Match(p)
        results.append(m.play_3match())

    average = np.mean(results)

    return average

def run_sim_range_classic(start, end, n):
    x = np.linspace(start, end, 50)
    output = []
    for i in x:
        output.append(1-run_sim(i,n))

    plt.plot(x, output, 'b-')
    plt.xlabel('probability of winning a given point')
    plt.ylabel('probability of winning match')
    #plt.axvline(.5)
    #plt.axhline(.5)
    plt.show()

#testing

run_sim_range_classic(.4, .6, 3000)










#testing
#this is so cool! I'm replicating the result I saw on a blog long ago.
#next step is to add the graphing functionality.
#print(1-run_sim(.505, 1000))

#print(np.linspace(.4, .60, 20))
