my_list = []
for i in range(2200, 3200):
    if i % 7 == 0 and i % 5 != 0:
        my_list.append(i)
print(my_list)
