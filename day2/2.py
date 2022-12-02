score = 0
points = {'X': 1, 'Y': 2, 'Z': 3}
success_case = {'A': 2, 'B': 3, 'C': 1}
fail_case = {'A': 3, 'B': 1, 'C': 2}
draw_case = {'A': 1, 'B': 2, 'C': 3}
line = input()

while line:
    opp, end_game = line.split()

    if end_game == 'X':
        score += fail_case[opp]
    elif end_game == 'Y':
        score += draw_case[opp] + 3
    else:
        score += success_case[opp] + 6

    line = input()

print(score)
