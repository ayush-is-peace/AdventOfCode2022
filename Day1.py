file = open('Day1_input.txt','r')
list1 = [x for x in file.read().splitlines()]
add = 0
list2 = []
for x in list1:
    if x != '':
        add += int(x)
    else:
        list2.append(add)
        add = 0
list3 = list2.copy()
print(max(list2))
list3.sort()
print(list3[-1]+list3[-2]+list3[-3])
