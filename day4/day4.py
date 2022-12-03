from collections import Counter
#first puzzle
def first(values):

    numbers = values[0]
    numbers = numbers.split(',')
    games_number = int((len(values)-1)/6)
    board =[]
    for i in range(games_number):
        j=i+2
    print(numbers)
    return -1

#second puzzle
def second(values):
    

    return -1


#################
input_file = open("day4/day4input.txt", "r")
content = input_file.read()
values = content.split("\n")
print("First puzzle result:")
print(first(values))
print("Second puzzle result:")
print(second(values))