def fileOpen():
    while True:
        fName = input("Enter file name, or type 'Exit Program': ")
        if fName == 'Exit Program':
            quit()
        else:
            try:
                fHand = open(fName)
                return fHand
            except:
                print('Invalid file name:', fName)

fHand = fileOpen()
di = dict()
lst = []

for line in fHand:
    if line.startswith('From '):
        time = line.split()[5]
        hour = time.split(':')[0]
        di[hour] = di.get(hour, 0) + 1

for (k, v) in di.items():
    tup = (k, v)
    lst.append(tup)
    lst = sorted(lst)

for set in lst:
    print(set[0], set[1])
