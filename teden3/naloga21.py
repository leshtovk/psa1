(N, D) = tuple(map(int, input().split()))
residents = tuple(map(int, input().split()))

def prepare(residents):
    lots = set(residents)

    housing = dict()
    for r in residents:
        housing[r] = housing.get(r, 0) + 1

    multiples = []
    singles = []
    for lot in lots:
        if housing.get(lot) > 1:
            multiples.append((lot, housing.get(lot)))
        else:
            singles.append(lot)

    return (lots, multiples, singles)

# ----------------------------------------------------------------

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def choose2(n):
    return fact(n)/(2 * fact(n-2))

# ----------------------------------------------------------------

def unique_nbs(lots, multiples, singles):
    counter = 0

    for m in multiples:
        lot = m[0]
        nbd = set(range(lot - D, lot + D + 1)).intersection(lots) - {lot}
        lots = lots - {lot}
        counter = counter + (m[1] * len(nbd)) + int(choose2(m[1]))
        # print("lot", lot, nbd, "candidates", lots, "counter", counter)

    for lot in singles:
        nbd = set(range(lot - D, lot + D + 1)).intersection(lots) - {lot}
        lots = lots - {lot}
        counter = counter + len(nbd)
        # print("lot", lot, nbd, "candidates", lots, "counter", counter)

    print(counter)

(l, m, s) = prepare(residents)
unique_nbs(l, m, s)
