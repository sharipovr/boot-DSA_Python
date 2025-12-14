class Trie:
    def add(self, word):
        """
        Adds a word to the trie.
        
        Steps:
        1. Start at the root
        2. For each character in the word, create nested dictionaries if needed
        3. Mark the end of the word with the end_symbol
        """
        # Keep track of your "current level" in the trie, starting at the root
        current_level = self.root
        
        # Loop over each character in the word-to-add
        for char in word:
            # If the character is not a key in the current level, add it and create a new nested level (dictionary) for it
            if char not in current_level:
                current_level[char] = {}
            
            # Update your "current level" to the nested dictionary for this character (whether it was just created or already existed)
            current_level = current_level[char]
        
        # Once you've ensured all the dictionaries exist, add the self.end_symbol to the dictionary of the last character in the word
        # This will indicate that this is a complete word and not just a prefix of another word
        current_level[self.end_symbol] = True

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"
