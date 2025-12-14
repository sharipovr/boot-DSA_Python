class HashMap:
    def key_to_index(self, key):
        """
        Converts a string key to an index in the hashmap.
        
        Steps:
        1. Calculate the sum of Unicode values of all characters in the key
        2. Mod the sum by the size of the hashmap to get the index
        3. Return the index
        """
        # Calculate the sum of Unicode values of all characters
        unicode_sum = sum(ord(char) for char in key)
        
        # Mod by the size of the hashmap to get the index
        index = unicode_sum % len(self.hashmap)
        
        return index

    def insert(self, key, value):
        """
        Inserts a key-value pair into the hashmap using linear probing for collision handling.
        """
        # Update the insert method to call resize before inserting a new key-value pair
        self.resize()
        
        # Compute the index for the key in the hashmap
        index = self.key_to_index(key)
        # Create an original_index variable and assign index to it
        original_index = index
        
        # Initialize a boolean variable first_iteration to True
        first_iteration = True
        
        # Begin a while loop that continues as long as the hashmap's slot at index is occupied (not None) and its key doesn't match the key being inserted
        while self.hashmap[index] is not None and self.hashmap[index][0] != key:
            # If this is not the first iteration and the current index equals original_index, raise an exception
            if not first_iteration and index == original_index:
                raise Exception("hashmap is full")
            
            # Increment index by 1 and wrap it around to the start of the hashmap if necessary (using modulo operation with hashmap's length)
            index = (index + 1) % len(self.hashmap)
            
            # Set first_iteration to False after the first iteration
            first_iteration = False
        
        # Insert the key-value pair at the found index
        self.hashmap[index] = (key, value)

    def get(self, key):
        """
        Retrieves the value associated with a key from the hashmap using linear probing.
        """
        # Compute the index for the key in the hashmap
        index = self.key_to_index(key)
        # Create an original_index variable and assign index to it
        original_index = index
        
        # Initialize a boolean variable first_iteration to True
        first_iteration = True
        
        # Begin a while loop that continues as long as the hashmap's slot at index is occupied (not None)
        while self.hashmap[index] is not None:
            # If the key at the current index matches the key being searched, return the value
            if self.hashmap[index][0] == key:
                return self.hashmap[index][1]
            
            # If this is not the first iteration and the current index equals original_index, raise an exception
            if not first_iteration and index == original_index:
                raise Exception("sorry, key not found")
            
            # If the key does not match, increment index by 1 and wrap it around to the start of the hashmap if necessary (using modulo operation with hashmap's length)
            index = (index + 1) % len(self.hashmap)
            
            # Set first_iteration to False after the first iteration
            first_iteration = False
        
        # If the while loop completes without finding a match, raise an exception
        raise Exception("sorry, key not found")

    def current_load(self):
        """
        Returns the number of filled buckets as a ratio of the total number of buckets.
        
        Steps:
        1. Count the number of filled buckets (not None)
        2. If length is 0, return 1
        3. Otherwise, divide filled buckets by total length
        """
        # Count the number of filled buckets (not None)
        filled_buckets = sum(1 for bucket in self.hashmap if bucket is not None)
        
        # If the length of the underlying list is zero, return 1
        if len(self.hashmap) == 0:
            return 1
        
        # Otherwise, divide the number of filled buckets by the length of the underlying list
        return filled_buckets / len(self.hashmap)

    def resize(self):
        """
        Resizes the hashmap if the load factor is >= 5%.
        
        Steps:
        1. If length is 0, make it 1 and return
        2. Get current load
        3. If load < 5%, do nothing
        4. Otherwise, resize to 10x and re-insert all pairs
        """
        # If the length of the underlying hashmap is 0, make the length 1 and return
        if len(self.hashmap) == 0:
            self.hashmap = [None]
            return
        
        # Get the current load
        load = self.current_load()
        
        # If it's less than 5%, do nothing, we have plenty of space
        if load < 0.05:
            return
        
        # Don't resize if hashmap is very small (allows small hashmaps to get full for testing)
        if len(self.hashmap) < 10:
            return
        
        # Otherwise, we need to resize the hashmap
        # Store the current hashmap in a temporary variable
        temp_hashmap = self.hashmap.copy()
        
        # Create a new empty hashmap that's 10x the size of the current one
        new_size = len(self.hashmap) * 10
        self.hashmap = [None for i in range(new_size)]
        
        # Re-insert all the key-value pairs from the temporary variable into self.hashmap
        for bucket in temp_hashmap:
            if bucket is not None:
                key, value = bucket
                self.insert(key, value)

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def __repr__(self):
        buckets = []
        for v in self.hashmap:
            if v != None:
                buckets.append(v)
        return str(buckets)