from collections import Counter
#first puzzle
def first(values):
    l = len(values[0])
    i = 0

    #inizialization of variables
    zeros = [0] * l
    ones = [0] * l
    
    gamma = ""
    epsilon = ""

    #for each value we count the number of ones and of zeroes in each position
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
    #for each bit you check if there are more zeroes or more ones and fill gamma and epsilon
    while pos < l:
        if zeros[pos] > ones[pos]:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
        pos = pos + 1
    #convert to decimal    
    g = int(gamma,2)
    e = int(epsilon,2)
    return g*e

#second puzzle
def second(values):
    #inicialization of variables
    l = len(values[0])
    i=0
    oxygen = values
    co2 = values

    #oxygen calc
    for i in range(l):
        a1=[]
        a2=[]
        #check that oxygen has more than one element left
        if len(oxygen) > 1:
            #for each bit divide the array on two arrays: one for those elements where the bit is a 0 and those where it is a 1
            for o in oxygen:
                if o[i]=='1':
                    a1.append(o)
                else:
                    a2.append(o)
            #if there are more 1s oxygen is a1. If the number of 0s and 1s is the same oxygen is a1. Else oxygen is a2.
            if len(a1)>=len(a2):
                oxygen = a1
            else:
                oxygen = a2
    i = 0

    while i < l:
        a1 = []
        a2 = []
        if len(co2)>1:
            #for each bit divide the array on two arrays: one for those elements where the bit is a 0 and those where it is a 1
            for c in co2:
                if c[i]=='0':
                    a1.append(c)
                else:
                    a2.append(c)
            #if there are less 0s than 1s or same number of 0s and 1s: c02 is a2. Else is a1
            if len(a1)>len(a2):
                co2 = a2
            else:
                co2 = a1
        i = i+1
    #convert to decimal
    ox = int(oxygen[0],2)
    diox = int(co2[0],2)
    #calculate value
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