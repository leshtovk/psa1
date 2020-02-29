(N, Z, K, S) = tuple(map(int, input().split()))

narocila = [[0, 0] for i in range(N)]
for i in range(N): 
    narocila[i] = tuple(map(int, input().split()))

num_of_days = narocila[-1][0]
orders = [0 for i in range(num_of_days)]
for i in range(N):
    orders[narocila[i][0] - 1] = narocila[i][1]
    
def strategy(num_of_days, orders, init_inventory, prod_capacity, storage_charge):
    """Compute the optimal strategy for filling all the orders, 
       assuming we don't sell any of the initial inventory."""
       
    order = inventory = orders[-1]
    production = 0
    
    debt = inventory * storage_charge
    strat = [[0, 0] for i in range(num_of_days - 2, -1, -1)] + [[inventory, production]]
    
    for i in range(num_of_days - 2, -1, -1):    
        order = orders[i]
        production = min(prod_capacity, inventory)
        inventory = inventory + order - production
        
        debt = debt + (inventory * storage_charge)
        strat[i] = [inventory, production]
        
    inventory = init_inventory
    if inventory < order: return (strat, -1)
    else: return (strat, debt)
     
def optimal_strategy(num_of_days, orders, init_inventory, storage_charge, strategy, debt):
    """Account for storing the initial inventory"""
    
    if debt == -1: print(-1)
    else: 
        total_orders = sum(orders)
        if init_inventory > total_orders: init_inventory = total_orders
        
        for i in range(1, num_of_days): 
            day_i_production = strategy[i-1][1]
            if day_i_production != 0 and init_inventory != 0:
            
                if day_i_production >= init_inventory:
                    debt = debt + (init_inventory * i * storage_charge)
                    init_inventory = 0
                    
                else:
                    debt = debt + (day_i_production * i * storage_charge)
                    init_inventory = init_inventory - day_i_production
        
        print(debt)

strategy, debt = strategy(num_of_days, orders, Z, K, S)
optimal_strategy(num_of_days, orders, Z, S, strategy, debt)
