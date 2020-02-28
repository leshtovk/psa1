# everything that is in stock has been stored before the year begins 
# we also have the list of orders before the year begins 
# we have to look at the list and see if we have anything in stock that 
# we can't sell within the year and destroy it before we get charged for it

(N, Z, K, S) = map(int, input().split())

narocila = []
for i in range(N):
    narocila.append(tuple(map(int, input().split())))
# `narocila` is a list that contains `(Di, Xi)` as its elements

storage = 0
bills = 0

# to create an optimal strategy we first need to know the total amount 
# of products that we have to sell 
# 
# it also lets us know if we have too many in stock 

def test_viability(orders): 

    total = sum([orders[i][1] for i in range(len(orders))])
    
    if Z > total:
        stock = total
        for i in range(len(orders)): 

            day_i = orders[i][0]
            order_i = orders[i][1]
            stock = stock - order_i
            print("day", day_i, "order", order_i, "stock", stock)

    else: 
        for i in range(len(orders)): 

            day_i = orders[i][0]
            order_i = orders[i][1]
            stock = Z + (day_i - 1) * K - sum([narocila[j][1] for j in range(i)])

            if order_i > stock:         
                print(-1)
                break 
            else:
                print("day", day_i, "order", order_i, "stock", stock)


test_viability(narocila)

# test if we have too many products in stock 






