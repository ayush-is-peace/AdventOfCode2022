print("########## Round 1 ########")
file = open("Day4_input.txt", 'r')
elfIds = [x for x in file.read().splitlines()]
elfId1, elfId2, pair1, pair2 = [], [], 0, 0
for x in elfIds:
    elfId1.append(x.split(','))
for x in elfId1:
    start, end = 0, 0
    group1, group2 = [], []
    s1, s2 = (), ()
    for j in range(len(x)):
        start, end = (x[j].split('-'))
        if j == 0:
            group1 = list(range(int(start),((int(end)+1))))
        else:
            group2 = list(range(int(start),((int(end)+1))))   
    s1 = set(group1)
    s2 = set(group2)
    if (len(list(s1.intersection(s2))) == len(list(s2)) or (len(list(s2.intersection(s1))) == len(list(s1)))):
        pair1 += 1
print(pair1)
print("########## Round 2 ########")
for x in elfIds:
    elfId2.append(x.split(','))
for x in elfId2:
    start, end = 0, 0
    group1, group2 = [], []
    s1, s2 = (), ()
    for j in range(len(x)):
        start, end = (x[j].split('-'))
        if j == 0:
            group1 = list(range(int(start), ((int(end)+1))))
        else:
            group2 = list(range(int(start), ((int(end)+1))))
    s1 = set(group1)
    s2 = set(group2)
    if(len(list(s1.intersection(s2))) >= 1 or (len(list(s2.intersection(s1))) >= 1)):
        pair2 += 1
print(pair2)
