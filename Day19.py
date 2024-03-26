def longest_value(dict1):
    longest = ''
    for value in dict1.values():
        if len(value) > len(longest):          
            longest = value
            return longest

fruits = {'fruit': 'apple', 'color': 'green'}
longest_value(fruits)