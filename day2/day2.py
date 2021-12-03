#first puzzle
def first(orders):
    horizontal = 0
    depth = 0
    l = len(orders)
    i = 0
    while i < l:
        ins = orders[i].split()
        if ins[0] == "forward":
            horizontal = horizontal+ int(ins[1])
        elif ins[0]== "up":
            depth = depth - int(ins[1])
        else:
            depth = depth + int(ins[1])
        i = i+1
    pos = horizontal * depth
    return pos

#second puzzle
def second(orders):
    horizontal = 0
    depth = 0
    aim = 0
    l = len(orders)
    i = 0
    while i < l:
        ins = orders[i].split()
        if ins[0] == "forward":
            horizontal = horizontal + int(ins[1])
            depth = depth + (aim * int(ins[1]))
        elif ins[0]== "up":
            aim = aim - int(ins[1])
        else:
            aim = aim + int(ins[1])
        i = i+1
    pos = horizontal * depth
    return pos


#################
input_file = open("day2input.txt", "r")
content = input_file.read()
orders = content.split("\n")
print("First puzzle result:")
print(first(orders))
print("Second puzzle result:")
print(second(orders))