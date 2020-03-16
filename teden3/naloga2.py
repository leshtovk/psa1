def count_nbs(nbd, D):
    counter = 0
    for i in range(len(nbd)):
        for p in nbd[i+1:]:
            if abs(nbd[i] - p) <= D:
                counter = counter + 1
    print(counter)

def main():
    (N, D) = tuple(map(int, input().split()))
    nbd = tuple(map(int, input().split()))
    count_nbs(nbd, D)

main()

