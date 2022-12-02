score = 0
points = {'X': 1, 'Y': 2, 'Z': 3}
line = input()

while line:
    opp, player = line.split()
    if (opp == 'A' and player == 'Y') or (opp == 'B' and player == 'Z') or (opp == 'C' and player == 'X'):
        score += points[player] + 6
    elif (opp == 'A' and player == 'X') or (opp == 'B' and player == 'Y') or (opp == 'C' and player == 'Z'):
        score += points[player] + 3
    else:
        score += points[player]

    line = input()

print(score)
