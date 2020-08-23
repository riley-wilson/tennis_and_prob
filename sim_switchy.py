import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from switchy_match import *
from collections import deque

#simulation of the streaky match.

def run_sim_switchy(p, p1, n):
    results = []

    for i in range(n):
        m = Match_Switch(p,p1)
        results.append(m.play_3match())

    return 1-np.mean(results)


def run_sim_switchy_range(n):
    y = np.linspace(.5, 1, 16) #switchy probabilities
    x = np.linspace(.4, .6, 16) #first point probabilities

    results = np.zeros((16, 16)) # creates zero'd 10x10 array

    for i, u in enumerate(y):
        l = []
        for j in x:
            l.append(run_sim_switchy(j, u, n))
        arr = np.array(l)
        results[15-i] = arr


    #graphing

    fig, ax = plt.subplots()
    im = ax.imshow(results, cmap = 'hot')

    plt.xlabel('probability of winning first point (p)')
    plt.ylabel('ps')

    #getting axis labels
    xaxis = []
    yaxis = deque()
    for i,f in enumerate(x):
        if i % 2 ==0:
            xaxis.append(str(round(f, 2)))
        else:
            xaxis.append('')
    for j, k in enumerate(y):
        if j %3 ==0:
            yaxis.appendleft(str(round(k, 2)))
        else:
            yaxis.appendleft('')

    #setting ticks
    ax.set_xticks(np.arange(16))
    ax.set_yticks(np.arange(16))

    #labeling ticks
    ax.set_xticklabels(xaxis)
    ax.set_yticklabels(yaxis)

    #colorbar
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel('Probability of winning match',rotation=-90, va="bottom")
    plt.show()



#works!
run_sim_switchy_range(2500)
