numbers = [10, 20, 10, 30, 10, 40]
search = int(input("Enter element: "))
count = 0
for i in numbers:
    if i == search:
        count = count + 1
print("Occurrences =", count)

#every no
numbers = [10, 20, 10, 30, 20, 40]

checked = []

for i in numbers:
    if i not in checked:
        count = 0

        for j in numbers:
            if i == j:
                count = count + 1

        print(i, ":", count)
        checked.append(i)