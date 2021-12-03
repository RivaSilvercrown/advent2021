#first puzzle
def first(values):

    return 1

#second puzzle
def second(values):

    return 0


#################
input_file = open("day3input.txt", "r")
content = input_file.read()
values = content.split("\n")
print("First puzzle result:")
print(first(values))
print("Second puzzle result:")
print(second(values))