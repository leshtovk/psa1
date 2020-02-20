# N -- length of the competition in minutes
# K -- length of the interruption in minutes
# L -- number of teams in the competition

# get a matrix of the numerical input data
def parse_input(fname):
    
    fhandle = open(fname)
    i = 1
    X = []
    
    for ln in fhandle:
        if i % 2 == 1:
            strings = ln.split()
            ints = []
            
            for j in range(len(strings)):
                ints.append(int(strings[j]))
            X.append(ints)
        
        i = i + 1
        
    return X

# get all the possible scores for a team
def get_scores(eff, K):
    # `eff` is a list of a team's minute-by-minute effectiveness 
    scores = []
    
    for i in range(len(eff) - K + 1):
        # `i` is the second when the interruption starts
        score = 0

        # add up the effectiveness from the 'active' minutes
        for j in range(len(eff)):
            if j not in range(i, i+K): 
                score = score + eff[j]
        scores.append(score) 

    return scores
    
# get a matrix that contains the possible scores of the teams as rows
# 
# then the j-th column (starting at 0) is the outcome of the competition
# in the case of the interruption starting on the j-th second
def outcomes(fname):

    X = parse_input(fname)
    Y = []
    K = X[0][1]
    
    for i in range(X[0][2]):
        # skip the first row of X, which contains N, K, L
        Y.append(get_scores(X[i+1], K))
    
    return Y
    
# get the best possible placement for the first team
def best_placement(Y): 
    
    placements = []
    
    for i in range(len(Y[0])):
        column_i = []
        
        for j in range(len(Y)):
            column_i.append(Y[j][i])
        
        # sort the list in descending order to get the first index 
        # that matches the score of the first team
        column_i.sort(reverse = True)
        placement = column_i.index(Y[0][i]) + 1
        placements.append(placement)
            
    return min(placements)
    
    
fname = input('Enter a file name: ')
Y = outcomes(fname)
print(best_placement(Y))