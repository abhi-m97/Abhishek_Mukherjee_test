import datetime
import time

#Question C of Technical Test

class LRUCache(object):

    #Initializes a Cache with the provided max size, and expiry time (seconds)
    def __init__(self, max_size=256, expiry_time=100):
        self.max_size = max_size
        self.expiry_time = expiry_time
        self.values = {}
        self.timestamps = {}

    #Adds an item to the cache
    def add(self,key,value):
        self.timestamps[key] = datetime.datetime.now()
        self.values[key] = value
        self.update()

    #Returns the size of the cache
    def size(self):
        return len(self.values)

    #Removes any items that have passed the expiry time
    def past_expiry(self):
        to_delete = []
        for k in self.timestamps.keys():
            if datetime.datetime.now() > self.timestamps[k] + datetime.timedelta(seconds=self.expiry_time):
                to_delete.append(k)
        for i in to_delete:
            del self.values[i]
            del self.timestamps[i]

    #Removes expired entries, and oldest entries if max size has been exceeded
    def update(self):
        self.past_expiry()

        while self.size() > self.max_size:
            oldest = datetime.datetime.now()
            oldest_key = 0
            for k in self.values.keys():
                if datetime.datetime.strptime(str(self.timestamps[k]),'%Y-%m-%d %H:%M:%S.%f') < oldest:
                    oldest = self.timestamps[k]
                    oldest_key = k
            del self.values[oldest_key]
            del self.timestamps[oldest_key]

    #Returns True if the key exists, False otherwise            
    def exists(self,key):
        return key in self.values

    #Returns the timestamp of a given key if it exists
    def get_timestamp(self, key):
        if self.exists(key):
            return self.timestamps[key]
        else:
            print("Entry doesn't exist")
            return None

    #Returns the timestamp of a given key if it exists
    def get_value(self, key):
        if self.exists(key):
            return self.values[key]
        else:
            print("Entry doesn't exist")
            return None

    #Clears all items in the cache
    def clear(self):
        self.values.clear()
        self.timestamps.clear()

    #Prints the keys, values and timestamps of every entry in the cache
    def display(self):
        self.update()
        print("-"*50)
        if len(self.values) > 0:
            for k in self.timestamps.keys():
                print("Key: " + k)
                print("Value: " + str(self.values[k]))
                print("Timestamp: " + str(self.timestamps[k]))
                print("-"*50)
        else:
            print("Cache is empty")
            print("-"*50)