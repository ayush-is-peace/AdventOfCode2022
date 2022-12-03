print("######## Round 1 ###########")
file = open('Day3_input.txt', 'r')
rucksacks = [x for x in file.read().splitlines()]
compartment1, compartment2 = [], []
lower_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
upper_dict = {'A':27, 'B':28, 'C':29, 'D':30, 'E':31, 'F':32, 'G':33, 'H':34, 'I':35, 'J':36, 'K':37, 'L':38, 'M':39, 'N':40, 'O':41, 'P':42, 'Q':43, 'R':44, 'S':45, 'T':46, 'U':47, 'V':48, 'W':49, 'X':50, 'Y':51, 'Z':52}
priorities1 = []
for sacks in rucksacks:
    length = len(sacks)
    compartment1.append(sacks[ :(length//2)])
    compartment2.append(sacks[(length//2): ])
for i in range(len(compartment1)):
    priority = []
    for letter in compartment1[i]:
        if(letter in compartment2[i]):
            if(letter not in priority):
                priority.append(letter)
                if(letter.islower()):
                    priorities1.append(int(lower_dict.get(letter)))
                else:
                    priorities1.append(int(upper_dict.get(letter)))
print(sum(priorities1))
print("########## Round 2 ############")
priority1, priority2, priority3 = [], [], []
priorities2 = []
group = 1
for i in range(len(rucksacks)):
    if group == 1:
        priority1.append(rucksacks[i])
        group += 1
    elif group == 2:
        priority2.append(rucksacks[i])
        group += 1
    else:
        priority3.append(rucksacks[i])
        group = 1
for i in range(len(priority1)):
    prior = []
    for badge in priority1[i]:
        if((badge in priority2[i]) and (badge in priority3[i])):
            if badge not in prior:
                prior.append(badge)
                if badge.islower():
                    priorities2.append(int(lower_dict.get(badge)))
                else:
                    priorities2.append(int(upper_dict.get(badge)))
print(sum(priorities2))
