# import timeit

# start_time = timeit.default_timer()

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