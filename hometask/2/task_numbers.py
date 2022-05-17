list1 = []
list2 = []
for number in range(10):
    if number % 2 == 0:
        list1.append(number)
    else:
        list2.append(number)

print(list1, list2)