
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]


occurrences = {}


for number in numbers:
    if number in occurrences:
        occurrences[number] += 1
    else:
        occurrences[number] = 1


print("Occurrences of each number:", occurrences)

