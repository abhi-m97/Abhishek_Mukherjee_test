#Question B of Technical Test

def version_checker(string1,string2):
    #I will assume the two inputs are two strings with numbers seperated by periods
    if type(string1) != str or type(string2) != str:
        raise TypeError("Please enter two strings containing version numbers")

    #If the input string starts with a period, a zero will be added in the beginning
    #i.e. a ".7" will turn into a "0.7"
    if string1[0] == ".":
        string1 = "0" + string1
    if string2[0] == ".":
        string2 = "0" + string2

    try:
        #Seperates the strings into arrays
        version1_temp = string1.split(".")
        version2_temp = string2.split(".")
        version1 = []
        version2 = []

        #Changes the type of the split array into int
        for i in version1_temp:
            version1.append(int(i))
        for i in version2_temp:
            version2.append(int(i))
    except:
        raise ValueError("Ensure strings comprise of numbers seperated by periods")

    #Finds the shorter array to loop through
    if len(version1) < len(version2):
        shorter_v = version1
        sv = string1
        longer_v = version2
        lv = string2
    else:
        shorter_v = version2
        sv = string2
        longer_v = version1
        lv = string1

    index = 0

    #Loops through the shorter array checking each value
    for i in shorter_v:
        if i < longer_v[index]:
            return "{} is greater than {}".format(lv,sv)
        elif i > longer_v[index]:
            return "{} is greater than {}".format(sv,lv)
        index += 1

    #If one array is longer, but the previous values were all the same, loops through it afterwards, if any values are non-zero the longer array is larger
    #Else, the two arrays are equal
    for i in longer_v[index:]:
        if i > 0: #If any of the values 
            return "{} is greater than {}".format(lv,sv)

    return "{} and {} are equal".format(sv,lv)

