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
    co2 = values

    while i < l:
        a1=[]
        a2=[]
        for o in oxygen:
            if o[i]=='1':
                a1.append(o)
                oxygen.pop()
            else:
                a2.append(o)
                oxygen.pop()
        if len(a1)>=len(a2):
            oxygen = a1
        else:
            oxygen = a2
        i = i+1
    i = 0

    while i < l:
        a1 = []
        a2 = []
        if len(co2)>1:
            for c in co2:
                if c[i]=='0':
                    a1.append(c)
                    co2.pop()
                else:
                    a2.append(c)
                    co2.pop()
            if len(a1)<=len(a2):
                if len(a1)>=1:
                    co2 = a1
            else:
                if len(a2)>=1:
                    co2 = a2
        i = i+1
    ox = int(oxygen[0],2)
    diox = int(co2[0],2)
    lifesupport =  ox*diox

    return lifesupport


#################
input_file = open("day3/day3input.txt", "r")
content = input_file.read()
values = content.split("\n")
print("First puzzle result:")
print(first(values))
print("Second puzzle result:")
print(second(values))