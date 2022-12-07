line = input()
count = 0


while line:
    part1, part2 = line.split(',')
    a, b = part1.split('-')
    c, d = part2.split('-')
    a, b, c, d = int(a), int(b), int(c), int(d)

    if not (b < c or a > d):
        count += 1

    line = input()

print(count)
