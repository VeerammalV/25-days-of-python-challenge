def convert_add(list1:list):
    list2 = []
    count = 0
    for i in list1:
        list2.append(int(i))
    for j in list2:
            count += j
    return count

print(convert_add(['1','3','5']))