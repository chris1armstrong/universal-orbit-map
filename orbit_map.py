from collections import defaultdict

if __name__ == "__main__":

    #build satellite dictionary from lines of input in format 'AAA)BBB', where BBB orbits AAA
    #input builds a tree graph with COM as the root, also including YOU and SAN (only important in part 2)
    satellites = defaultdict(list)
    with open('input.txt','r') as f:
        for line in f:
            center,orbiter = line.strip().split(')')
            satellites[orbiter] = center
    f.close()

    #count number of direct orbits, and number of indirect orbits
    #if AAA)BBB and BBB)CCC, then CCC directly orbits BBB but indirectly orbits AAA
    direct,indirect = 0,0
    for i in satellites:
        x = satellites[i]
        direct += 1
        while x != "COM":
            x = satellites[x]
            indirect += 1

    #find the number of orbits from YOU to COM, storing that number at each stage
    mypath = defaultdict(int)
    x = satellites["YOU"]
    dist = 0
    while x != "COM":
        dist += 1
        mypath[x] = dist
        x = satellites[x]

    #find the number of orbits from SAN to a satellite shared with mypath
    #calculate the number of transfers by the sum of values stored in
    #mypath and sanpath at the common key
    #subtract 2 to discount the orbits of YOU and SAN around their parents
    x = satellites["SAN"]
    dist = 0
    transfers = 0
    while x != "COM":
        dist += 1
        if mypath[x] != 0:
            transfers = mypath[x] + dist - 2
            break
        x = satellites[x]
    
    #output
    print("total direct =", direct)
    print("total indirect =", indirect)
    print("total =", direct + indirect)
    print("common orbit around",x)
    print("transfers from YOU to SAN =", transfers)
