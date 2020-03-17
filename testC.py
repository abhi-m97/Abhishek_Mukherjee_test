import datetime
import time
from questionC import LRUCache

#These are some test values of the question C class with their expected output commented
cache = LRUCache(3,5)
cache.add('a',1)
cache.add('b',2)
cache.add('c',3)
cache.display() #Output: Cache details, a, b, c

cache.clear()
cache.display() #Output: Cache is Empty
print("-"*50)

cache.add('a',1)
cache.add('b',2)
cache.add('c',3)
print(cache.size()) #Output: 3
print(cache.exists('a')) #Output: True
print(cache.exists('c')) #Output: True
print(cache.exists('d')) #Output: False
print(cache.get_value('a')) #Output: 1
print(cache.get_value('b')) #Output: 2
print(cache.get_timestamp('a')) #Output: Timestamp
print(cache.get_timestamp('b')) #Output: Timestamp
cache.add('d',4)
cache.display() #Output: Cache details, b, c, d without a
time.sleep(5) #A five second delay, to allow all the cached items to expire
cache.display() #Output: Cache is Empty