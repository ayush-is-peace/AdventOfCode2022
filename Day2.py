print("#######Round 1 #######")
file = open('Day2_input.txt','r')
list1 = [x for x in file.read().splitlines()]
score_dict = {'X':1, 'Y':2, 'Z':3}
score_list = [0,3,6]
list2, player2_score = [], []
for x in list1:
    list2 += x.split(' ')
player1 = [x for x in list2 if x == 'A' or x == 'B' or x == 'C']
player2 = [y for y in list2 if y == 'X' or y == 'Y' or y == 'Z']
for i in range(len(player2)):
    if((player1[i] == 'A' and player2[i] == 'Y') or (player1[i] == 'B' and player2[i] == 'Z') or (player1[i] == 'C' and player2[i] == 'X')):
        player2_score.append(int(score_dict.get(player2[i])) + score_list[2])
    elif((player1[i] == 'A' and player2[i] == 'Z') or (player1[i] == 'B' and player2[i] == 'X') or (player1[i] == 'C' and player2[i] == 'Y')):
        player2_score.append(int(score_dict.get(player2[i])) + score_list[0])
    else:
        player2_score.append(int(score_dict.get(player2[i])) + score_list[1])
print(sum(player2_score))
print("####### Round 2 ########")
final_score = []
for i in range(len(player1)):
    if(player2[i] == 'X'):
        if(player1[i] == 'A'):
            final_score.append(int(score_dict.get('Z')) + score_list[0])
        elif(player1[i] == 'B'):
            final_score.append(int(score_dict.get('X')) + score_list[0])
        else:
            final_score.append(int(score_dict.get('Y')) + score_list[0])
    elif(player2[i] == 'Y'):
        if(player1[i] =='A'):
            final_score.append(int(score_dict.get('X')) + score_list[1])
        elif(player1[i] == 'B'):
            final_score.append(int(score_dict.get('Y')) + score_list[1])
        else:
            final_score.append(int(score_dict.get('Z')) + score_list[1])
    else:
        if(player1[i] == 'A'):
            final_score.append(int(score_dict.get('Y')) + score_list[2])
        elif(player1[i] == 'B'):
            final_score.append(int(score_dict.get('Z')) + score_list[2])
        else:
            final_score.append(int(score_dict.get('X')) + score_list[2])
print(sum(final_score))
