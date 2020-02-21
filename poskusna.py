# N -- length of the competition in minutes
# K -- length of the interruption in minutes
# L -- number of teams in the competition
# X -- input matrix (list of tuples)
# Y -- output matrix (list of lists)

# get a matrix of the numerical input data -- the input matrix
def parse_input(fname):
    
    fhandle = open(fname)
    X = []
    i = 1
    
    for ln in fhandle:
        if i % 2 == 1:
            
            # split the line and store the data as integers 
            ln_data = tuple(map(int, ln.split()))            
            X.append(ln_data)
        
        i = i + 1
        
    return X

# get all the possible scores for a team
# `eff` is a list of a team's minute-by-minute effectiveness
def get_scores(eff, N, K):
     
    scores = []
    
    for i in range(N - K + 1):
        # `i` is the minute when the interruption starts
        score = 0
        inactive = range(i, i+K)

        # add up the effectiveness from the 'active' minutes
        for j in range(N):
            if j not in inactive: 
                score = score + eff[j]
        
        scores.append(score) 

    return scores
    
# get a matrix that contains the possible scores of the teams as rows -- the output matrix
# 
# the i-th column (starting at 0) is the outcome of the competition
# in the case of the interruption starting on the i-th minute
def outcomes(fname):

    X = parse_input(fname)
    (N, K, L) = (X[0][i] for i in range(3))
    Y = []
    
    for i in range(L):
        # skip the first row of X, which contains N, K, L
        Y.append(get_scores(X[i+1], N, K))
    
    # we're also returning `L` so we don't have to compute `len(Y)` in `best_placement`
    return (Y, L)
    
# get the best possible placement for the first team
def best_placement(Y, L): 
    
    placements = []
    
    # iterate over columns
    for i in range(len(Y[0])):
        column_i = []
        score = Y[0][i]
        
        for j in range(L):
            column_i.append(Y[j][i])
        
        # sort the column in descending order to get the first index 
        # that matches the score of the first team
        column_i.sort(reverse = True)
        placement = column_i.index(score) + 1
        placements.append(placement)
            
    return min(placements)
    
    
fname = input('Enter a file name: ')
(Y, L) = outcomes(fname)
print(best_placement(Y, L))