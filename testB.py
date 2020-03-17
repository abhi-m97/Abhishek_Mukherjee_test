from questionB import version_checker

#These are some test values of the question B function with their expected output commented
print(version_checker("1.2","1.1")) #1.2 is greater
print(version_checker("1.2","1.13")) #1.13 is greater
print(version_checker(".2","1.1")) #1.1 is greater
print(version_checker(".2",".1")) #.2 is greater
print(version_checker("1.2.4","1.1")) #1.2.4 is greater
print(version_checker("1.2","1.1.1.2")) #1.2 is greater
print(version_checker("1.2","1.2.3.3.4")) #1.2.3.3.4 is greater
print(version_checker(".2","0.2.0.0.0")) #Both are equal
print(version_checker("1.2","1.2.0.0.0")) #Both are equal