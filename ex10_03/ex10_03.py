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
alphabet = 'abcdefghijklmnopqrstuvwxyz'
di = {}
lst = []

for line in fHand:
    for letter in line:
        letter = letter.lower()
        if letter in alphabet:
            di[letter] = di.get(letter, 0) + 1
        else:
            continue

for (k, v) in di.items():
    tup = (v, k)
    lst.append(tup)
    lst = sorted(lst, reverse = True)

for set in lst:
    print(set[1], set[0])
