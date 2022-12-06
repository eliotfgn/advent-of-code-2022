import string

line = input()
val = list(string.ascii_lowercase)
val.extend(list(string.ascii_uppercase))
count = 0

while line:
    part1, part2 = set(line[0: len(line)//2]), set(line[len(line)//2:])

    for item in part1:
        if item in part2:
            count += val.index(item)+1
            break

    line = input()

print(count)
