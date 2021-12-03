#count the number of times a depth measurement increases
def depth_meter(str):
    #variable inicialization
    l = len(str)
    times = 0
    #we start our index by the second item (our array's first index is 0)
    i = 1
    #read the whole value range
    while i < l:
        #compare each item with the one preceding it
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
