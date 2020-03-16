(N, D) = tuple(map(int, input().split()))
residents = dict()
for i in map(int, input().split()):
    residents[i] = residents.get(i, 0) + 1

def neighbors(d, D):
    counter = 0
    lots = set(d.keys())
    for key in d.keys():
        nbd = list(set(range(key - D, key + D + 1)).intersection(lots) - {key})
        counter = counter + (d[key] * sum([d[i] for i in nbd])) + (d[key] - 1)
        lots = lots - {key}
    print(counter)

neighbors(residents, D)
