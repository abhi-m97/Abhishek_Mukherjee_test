from questionA import intersection_check

#These are some test values of the question A function with their expected output commented
print(intersection_check((1,2),(3,4))) #Output: False
print(intersection_check((1,2),(2,1))) #Output: True
print(intersection_check((1,5),(2,3))) #Output: True
print(intersection_check((-1,400),(7000,8000))) #Output: False 
print(intersection_check((800,801),(2,3))) #Output: False
print(intersection_check((4,5),(1,2))) #Output: False
print(intersection_check((1,6),(-5,7))) #Output: True
print(intersection_check((3,4),(1,4))) #Output: True