list_data = [8, 10, 6, 2, 4]

for i in range(len(list_data)):
    for j in range(0, len(list_data) - i - 1):
        if list_data[j] > list_data[j + 1]:
            list_data[j], list_data[j + 1] = list_data[j + 1], list_data[j]

print(list_data)