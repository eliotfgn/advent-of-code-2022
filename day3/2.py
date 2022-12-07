import string

line = input()
val = list(string.ascii_lowercase)
val.extend(list(string.ascii_uppercase))
i = 0
count = 0
group = []

while line:

    if i == 0:
        group = []

    group.append(set(line))
    i = (i+1) % 3

    if i == 0:
        res = []
        res.extend(group[0])
        res.extend(group[1])
        res.extend(group[2])
        badge = ''

        for letter in res:
            if res.count(letter) == 3:
                badge = letter
                break

        count += val.index(badge)+1

    line = input()

print(count)
