# import timeit

# start_time = timeit.default_timer()

# vhod:
#
# N K L
# u1 u2 ... uk
#
# N -- length of the competition in minutes
# K -- length of the interruption in minutes
# L -- number of teams in the competition
#
# Sample:
# 
# 4 2 2
# Ljubljana 1
# 60 20 10 1
# Varsava
# 100 100 100 100

import numpy as np 

def parse_input(fname):
    fhandle = open(fname)

    i = 1

    for ln in fhandle:
        if i == 1:
            NKL = ln.split()
           
           # N = NKL[0]
            #L = NKL[2]
            #effs = np.zeros(np.int32(N), np,.int32(L))
            
            #return effs



def get_scores(eff, K):

    scores = []
    for i in range(len(eff) - K + 1):
        score = 0

        for j in range(len(eff)):
            if j not in range(i, i+K): 
                score = score + eff[j]
        scores.append(score) 

    return scores

# elapsed = timeit.default_timer() - start_time