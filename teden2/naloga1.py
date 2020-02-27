(N, Z, K, S) = map(int, input().split())

# `narocila` is a list that contains `(Di, Xi)` as its elements
# amount of products that need to be produced: sum(Xi) - Z 

narocila = []

for i in range(N):
    narocila.append(tuple(map(int, input().split())))

storage = 0
bills = 0

# check if we can meet all the orders: 
#
# not correct yet
# figure out a way to add up the demand properly 
# and make sure to subtract previously filled orders 
# evey time you compute the cappacity 
# to get the true situation

for day in [narocila[i][0] for i in range(N)]:
    demand = sum(narocila[j][1] for j in range(i))
    produce_capacity = Z + (day * K)
    print("day", day, "demand", demand, "capacity", produce_capacity)





