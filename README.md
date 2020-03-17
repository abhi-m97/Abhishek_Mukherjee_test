# Abhishek_Mukherjee_test
Ormuco Technical Test

The files for the questions outlined in the email have been labelled as questionA.py, questionB.py, and questionC.py. Test files have also been included, with various test cases, and their expected outputs commented.

Question A:
Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).

Example:
print(intersection_check((1,2),(3,4))) #Output: False
print(intersection_check((1,5),(2,3))) #Output: True

Output:
False
True

Question B:
The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.

Example:
print(version_checker("1.2","1.1")) #1.2 is greater
print(version_checker("1.2","1.13")) #1.13 is greater

Output:
1.2 is greater than 1.1
1.13 is greater than 1.2

Question C:
At Ormuco, we want to optimize every bits of software we write. Your goal is to write a new library that can be integrated to the Ormuco stack. Dealing with network issues every day, latency is our biggest problem. Thus, your challenge is to write a new Geo Distributed LRU (Least Recently Used) cache with time expiration. This library will be used extensively by many of our services so it needs to meet the following criteria:

 

    1 - Simplicity. Integration needs to be dead simple.

    2 - Resilient to network failures or crashes.

    3 - Near real time replication of data across Geolocation. Writes need to be in real-time.

    4 - Data consistency across regions

    5 - Locality of reference, data should almost always be available from the closest region

    6 - Flexible Schema

    7 - Cache can expire 
   
Example:
cache = LRUCache(3,5)
cache.add('a',1)
cache.add('b',2)
cache.add('c',3)
cache.display() #Output: Cache details, a, b, c

Output:
--------------------------------------------------
Key: a
Value: 1
Timestamp: 2020-03-17 14:07:05.842670
--------------------------------------------------
Key: b
Value: 2
Timestamp: 2020-03-17 14:07:05.842670
--------------------------------------------------
Key: c
Value: 3
Timestamp: 2020-03-17 14:07:05.842670
--------------------------------------------------


Missing Functionality:
Instead of using two dictionaries, faster implementation can involve a doubly linked list, and one dictionary. In the future, this would allow for faster updating of the cache, by making it faster to find the oldest member in the cache, to replace, if a new entry is added, or if it's expiry has passed.
