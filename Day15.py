def sum_list():
    p1 =  [[2, 4, 5, 6], [2, 3, 5, 6]]
    p2 = [one for sublist in p1 for one in sublist]
    print(sum(p2))
def main():
    sum_list()


main()
