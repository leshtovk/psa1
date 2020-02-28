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

# test if we can fill all the orders, assuming we produce maximally every day 

def test_viability(orders): 

    for i in range(len(orders)): 
        
        day_i = orders[i][0]
        order_i = orders[i][1]
        produce_capacity = Z + (day_i - 1) * K - sum([narocila[j][1] for j in range(i)])
        
        print("day", day_i, "order", order_i, "capacity", produce_capacity)


test_viability(narocila)




