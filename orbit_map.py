from collections import defaultdict

if __name__ == "__main__":

    satellites = defaultdict(list)
    dummy = 0
    with open('input.txt','r') as f:
        for line in f:
            center,orbiter = line.strip().split(')')
            satellites[orbiter].append(center)
    f.close()
    for i in satellites:
        print(i + ': ' + str(satellites[i]))
