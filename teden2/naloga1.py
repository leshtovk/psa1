# everything that is in stock has been stored before the year begins 
# we also have the list of orders before the year begins 
# we have to look at the list and see if we have anything in stock that 
# we can't sell within the year and destroy it before we get charged for it

(N, Z, K, S) = map(int, input().split())

# `narocila` is a list that contains `(Di, Xi)` as its elements
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

def need_to_make(order, capacity): 
    return min(order, capacity)

def optimal_strategy(): 
    need = 0
    res = 0
    order = orders[-1]
    strategy = []

    for i in range(len(orders) - 2, -1, -1): 
        need = need_to_make(order, K) 
        res = order - need
        order = orders[i] + res

        strategy.append(need)   

    strategy.reverse()
    return strategy

#####################################################################################

def test_viability(): 
    
    if Z > total:

        stock = total    
        for i in range(N): 

            day_i = days[i]
            order_i = orders[i]
            stock = stock - order_i
            print("day", day_i, "order", order_i, "stock", stock)

    else:

        for i in range(N): 

            day_i = days[i]
            order_i = orders[i]
            stock = Z + (day_i - 1) * K - sum([orders[j] for j in range(i)])

            if order_i > stock:         
                print(-1)
                break 
            else:
                print("day", day_i, "order", order_i, "stock", stock)

            

# test_viability()
# print(days)
# print(shipping_days)
# print(orders)
print(optimal_strategy())