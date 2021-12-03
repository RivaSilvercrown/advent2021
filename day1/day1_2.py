#count the number of times a sliding sum for length 3 is bigger than the sliding sum before it
def depth_meter(str):
    #variable inicialization
    l = len(str)
    times = 0
    #we start our index by the 4th item (our array's first index is 0)
    i = 3
    #read the whole value range
    while i < l:
        #calculate both sliding sums
        sumA=int(str[i-3])+int(str[i-2])+int(str[i-1])
        sumB=int(str[i-2])+int(str[i-1])+int(str[i])
        if int(str[i-1])<int(str[i]):
            #if depth increases we count it
            times = times+1
        i = i+1
    return times


#now we enter our data
input_file = open("day1input.txt", "r")
content = input_file.read()
measurements = content.split("\n")
print(depth_meter(measurements))