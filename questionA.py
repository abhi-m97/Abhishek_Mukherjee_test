#Question A of Technical Test

def intersection_check(line1, line2):
    #I will assume the two inputs are two arrays of length 2, with the first point being the 
    #left most point and the second point being the right most point of the line
    if type(line1) != tuple or type(line2) != tuple:
        raise TypeError("Please enter two tuples containing the start and end points of the lines")
    if len(line1) != 2 or len(line2) != 2:
        raise ValueError("Ensure both tuples contain only 2 values")

    #First, the leftmost line will be determined. 
    #Checks if the rightmost part of the leftmost line is less than the leftmost part of the rightmost line
    if line1[0] < line2[0]:
        return line1[1] >= line2[0]
    elif line2[0] < line1[0]:
        return line2[1] >= line1[0]
    else:
        #If both lines' left point is the same, an intersection already exists 
        return True