class HashMap(object):
    def __init__(self, size):
        self.size = size
        self.index_to_item = [[] for _ in range(self.size)]

    def set(self, key, value):
        # Determine the hash index 
        index = self._hash(key)
        
        # For each item in this bucket
        for item in self.index_to_item[index]:
            # If the keys are equal
            if item.key == key:
                # Update the value
                item.value = value
                return
        
        # Item doesn't exist; construct and add a new item to the map
        self.index_to_item[index].append(Item(key, value))

    def get(self, key):
        # Determine the hash index
        index = self._hash(key)

        # For each item in this bucket
        for item in self.index_to_item[index]:
            # If the keys are equal
            if item.key == key:
                # Return the value
                return item.value
            
        # Item doesn't exist; return an error
        raise KeyError("Key not found")

    def remove(self, key):
        # Determine the hash index
        hash_index = self._hash(key)

        # For each item in this bucket
        for item_index, item in enumerate(self.index_to_item[hash_index]):
            # If the keys are equal
            if item.key == key:
                # Delete the item
                del self.index_to_item[hash_index][item_index]
                return
        
        # Item doesn't exist; return an error
        raise KeyError("Key not found")

    def _hash(self, key):
        return key % self.size
    
class Item(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value