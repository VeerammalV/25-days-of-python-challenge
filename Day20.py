def convert_add(stringList):
    convertList = [int(i) for i in stringList]
    return (f'The new list is {convertList}, and the sum is {sum(convertList)}')

u =  ['1', '3', '5']    
convert_add(u)