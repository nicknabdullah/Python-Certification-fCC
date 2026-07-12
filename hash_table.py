class HashTable:
    def __init__(self):
        self.collection = {}
    
    # return hash
    def hash(self, str_to_hash):
        return sum(ord(char) for char in str_to_hash)
    
    # add key-value under key_hash
    def add(self, key, value):
        key_hash = self.hash(key)
        if key_hash not in self.collection:
            self.collection[key_hash] = {key: value}
        else:
            self.collection[key_hash][key] = value
    
    # remove item of key
    def remove(self, key):
        key_hash = self.hash(key)
        if (key_hash in self.collection 
            and key in self.collection[key_hash]):
            del self.collection[key_hash][key]
    
    # return  value if key exists
    def lookup(self, key):
        key_hash = self.hash(key)
        if key_hash not in self.collection:
            return None
        if key in self.collection[key_hash]:
            return self.collection[key_hash][key]
