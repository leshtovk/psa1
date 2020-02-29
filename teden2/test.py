(N, Z, K, S) = tuple(map(int, input().split()))

narocila = [[0, 0] for i in range(N)]
for i in range(N): 
    narocila[i] = tuple(map(int, input().split()))

num_of_days = narocila[-1][0]
orders = [0 for i in range(num_of_days)]
for i in range(N):
    orders[narocila[i][0] - 1] = narocila[i][1]
    
print('No. of days:', num_of_days)
print('Orders:', orders)