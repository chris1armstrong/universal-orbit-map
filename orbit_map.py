from collections import defaultdict

if __name__ == "__main__":

    satellites = defaultdict(list)
    dummy = 0
    with open('input.txt','r') as f:
        for line in f:
            center,orbiter = line.strip().split(')')
            satellites[orbiter] = center
    f.close()
    direct,indirect = 0,0
    for i in satellites:
        x = satellites[i]
        direct += 1
        while x != "COM":
            x = satellites[x]
            indirect += 1

    mypath = defaultdict(int)
    x = satellites["YOU"]
    dist = 0
    while x != "COM":
        dist += 1
        mypath[x] = dist
        x = satellites[x]

    sanpath = defaultdict(int)
    x = satellites["SAN"]
    dist = 0
    transfers = 0
    while x != "COM":
        dist += 1
        sanpath[x] = dist
        if mypath[x] != 0:
            transfers = mypath[x] + dist - 2
            break
        x = satellites[x]
    

    print("total direct =", direct)
    print("total indirect =", indirect)
    print("total =", direct + indirect)
    print("transfers from YOU to SAN =", transfers)
