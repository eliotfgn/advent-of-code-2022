elves_calories = []
current_elf_calories = 0

while True:
    try:
        data = input()
        if data == "5509":
            break
    except EOFError:
        break

    if data:
        data = int(data)
        current_elf_calories += data
    else:
        elves_calories.append(current_elf_calories)
        current_elf_calories = 0

elves_calories.sort(reverse=True)

print(sum(elves_calories[0:3]))
