def check_duplicates(list_of_strings):
    for item in list_of_strings:
        if list_of_strings.count(item) > 1:
            return item
        else:
            return 'No duplicates'
# lists
fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']

print(check_duplicates(fruits))
print(check_duplicates(names))