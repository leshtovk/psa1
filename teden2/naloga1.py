
(N, Z, K, S) = tuple(map(int, input().split()))

narocila = [[0, 0] for i in range(N)]
for i in range(N): 
    narocila[i] = tuple(map(int, input().split()))

num_of_days = narocila[-1][0]

# `orders` is a list of all the orders from `narocila` 
# where the element in position i is the order for day (i+1) 
orders = [0 for i in range(num_of_days)]
for i in range(N):
    orders[narocila[i][0] - 1] = narocila[i][1]

def strategy():
    """Compute the optimal strategy for filling all the orders, 
       assuming we don't sell any of the initial inventory."""
       
    order = inventory = orders[-1]
    production = 0
    strat = [[0, 0, 0] for i in range(num_of_days - 2, -1, -1)] + [[inventory, production, order]]
    
    for i in range(num_of_days - 2, -1, -1):    
        order = orders[i]
        production = min(K, inventory)
        inventory = inventory + order - production
        strat[i] = [inventory, production, order]
            
    if Z < inventory: return -1
    else: return strat
     
     
def adjust_strategy(strategy, Z):
    """Include the initial inventory in the strategy obtained by `strategy()`"""

    if Z > sum(orders): Z = sum(orders)
    inventory = [strategy[i][0] for i in range(num_of_days)]
    production = [strategy[i][1] for i in range(num_of_days)]
    
    for i in range(num_of_days - 1):
        if i == 0: inventory[i] = Z
        
        if inventory[i+1] <= inventory[i] - orders[i]:
            production[i] = 0
            inventory[i+1] = inventory[i] - orders[i]
        else: 
            production[i] = inventory[i+1] - inventory[i] + orders[i]
        
        if orders[i] >= Z:
            Z = 0 
            break
        else: 
            Z = Z - orders[i]
            
    adjusted_strategy = [[inventory[i], production[i], orders[i]] for i in range(num_of_days)]
    return adjusted_strategy
    
def debt(optimal_strategy):
    """Calculate the debt that will be owed after filling all the orders"""
    
    debt = 0
    for i in range(num_of_days):
        debt = debt + optimal_strategy[i][0] * S
    
    return debt
    
    
strat = strategy()
if strat == -1: print(-1)
else: 
    optimal = adjust_strategy(strat, Z)
    print(debt(optimal))
    