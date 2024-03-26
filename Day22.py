def convert_add(list1):
    b = []
    for i in list1:
        b.append(int(i))
    return sum(b)

print(convert_add(['1','3','5']))