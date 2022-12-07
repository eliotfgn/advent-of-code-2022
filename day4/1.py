line = input()
count = 0


while line:
    part1, part2 = line.split(',')
    a, b = part1.split('-')
    c, d = part2.split('-')
    a, b, c, d = int(a), int(b), int(c), int(d)

    if (a <= c and b >= d) or (a >= c and b <= d):
        count += 1

    line = input()

print(count)
