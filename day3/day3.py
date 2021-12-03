from collections import Counter
#first puzzle
def first(values):
    l = len(values[0])
    i = 0

    zeros = [0] * l
    
    ones = [0] * l
    
    gamma = ""
    epsilon = ""
    for value in values:
        j = 0
        for digit in value:
            if digit=="1":
                ones[j]=ones[j]+1
            else:
                zeros[j]=zeros[j]+1
            j = j+1

        i = i+1
    pos = 0
    while pos < l:
        if zeros[pos] > ones[pos]:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
        pos = pos + 1
        
    g = int(gamma,2)
    e = int(epsilon,2)
    return g*e

#second puzzle
def second(values):
    l = len(values[0])
    i=0
    oxygen = values

    while i < l:
        a = Counter(ox[i] for ox in oxygen)
        c = list(a.keys())
        for ox in oxygen:
            if ox[i] == c[0]:
                oxygen.remove(ox)
        i = i+1
    print(oxygen)



    return 0


#################
input_file = open("day3/day3input.txt", "r")
content = input_file.read()
values = content.split("\n")
print("First puzzle result:")
print(first(values))
print("Second puzzle result:")
print(second(values))