#first puzzle
def first(orders):
    horizontal = 0
    depth = 0
    l = len(orders)
    i = 0
    while i < l:
        print(orders[i])
        i = i+1
    pos = horizontal * depth
    return pos

def new_func():
    return 1

#second puzzle
def second(orders):
    return 0


#################
input_file = open("day2input.txt", "r")
content = input_file.read()
orders = content.split("\n")
print(first(orders))