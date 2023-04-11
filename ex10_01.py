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
        line = line.split()
        email = line[1]
        di[email] = di.get(email, 0) + 1

for (k, v) in di.items():
    tup = (v, k)
    lst.append(tup)
    lst = sorted(lst, reverse = True)
    
most = lst[0]    
print(most[1], most[0])
