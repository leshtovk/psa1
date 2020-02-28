# everything that is in stock has been stored before the year begins 
# we also have the list of orders before the year begins 
# we have to look at the list and see if we have anything in stock that 
# we can't sell within the year and destroy it before we get charged for it

# ----------------- - ORGANIZE INPUT DATA -----------------------

(N, Z, K, S) = map(int, input().split())

narocila = []
for i in range(N):
    narocila.append(tuple(map(int, input().split())))

shipping_days = [narocila[i][0] for i in range(N)]
days = [i for i in range(1, shipping_days[-1] + 1)]

orders = []
j = 0
for i in range(len(days)):
    if days[i] in shipping_days:
        orders.append(narocila[j][1])
        j = j + 1
    else: 
        orders.append(0)

total = sum(orders)

# ---------------- FIND OPTIMAL STRATEGY -------------------------

def need_to_make(order, capacity): 
    return min(order, capacity)

def optimal_strategy(): 

    produce = 0
    residue = order = orders[-1]
    strat = [[0, order]]

    for i in range(len(orders) - 2, -1, -1): 

        produce = need_to_make(order, K) 
        residue = order - produce
        order = orders[i] + residue

        strat.append([produce, orders[i]])

    if residue > 0: 
        return -1
    else:
        strat.reverse()
        return strat

def use_stored(Z): 

    # destroy extra inventory if there is any 
    if Z > total: Z = total
    strat = optimal_strategy() 

    if strat == -1: 
        return strat
    else:
        i = 0
        while Z > 0 and i < len(strat):
            if strat[i][0] > 0: 
                strat[i][0] = strat[i][0] - 1
                Z = Z - 1
            i = i + 1

        return strat

    

print(use_stored(Z))