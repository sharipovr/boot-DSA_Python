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

    def exists(self, word):
        """
        Checks if a word exists in the trie.
        
        Steps:
        1. Start at the root
        2. Follow the path for each character in the word
        3. If any character is missing, return False
        4. Check if the end_symbol exists at the end
        """
        # Starting with the root of the trie, assign the current dictionary to a variable
        current = self.root
        
        # Loop over the letters in the word
        for letter in word:
            # If the current letter is not in the current dictionary, return False
            if letter not in current:
                return False
            
            # Update current to point to the dictionary at the letter key
            current = current[letter]
        
        # Once you get to the last letter, return True if end_symbol is in the current dictionary, and False if it isn't
        return self.end_symbol in current

    def search_level(self, level, prefix, words):
        """
        Recursive function that collects all complete words starting from the current trie level.
        
        Args:
            level: Current dictionary level in the trie
            prefix: Accumulated prefix so far
            words: Collection of words found (list that gets modified)
        
        Returns:
            All words found (the words list)
        """
        # Check for complete words
        # If the current level contains an end marker, add the current prefix to the words collection
        if self.end_symbol in level:
            words.append(prefix)
        
        # Process each character in the current level in sorted order (alphabetical)
        # For each character (except end markers)
        for char in sorted(level.keys()):
            if char != self.end_symbol:
                # Extend the prefix with the current character (e.g., current_prefix + character, rather than modifying the prefix in place)
                extended_prefix = prefix + char
                # Recursively search the child level with the extended prefix
                self.search_level(level[char], extended_prefix, words)
        
        # Return all words found
        return words

    def words_with_prefix(self, prefix):
        """
        Finds all words in the trie that begin with a given prefix.
        
        Args:
            prefix: The prefix to search for
        
        Returns:
            List of all words that start with the prefix
        """
        # Create an empty list to store matching words
        words = []
        
        # Keep track of the current trie level, starting at the root
        current_level = self.root
        
        # Iterate through each character in the prefix
        for char in prefix:
            # If the character doesn't exist in the current level, return an empty list: no words start with this prefix
            if char not in current_level:
                return []
            
            # If the character does exist, move to the child level corresponding to the current character
            current_level = current_level[char]
        
        # By now, the current level should correspond to the last character in the prefix
        # Use the search_level function to find all words starting from this level and return them
        self.search_level(current_level, prefix, words)
        return words

    def find_matches(self, document):
        """
        Finds all words from the trie that occur in the document.
        
        Args:
            document: The document string to search in
        
        Returns:
            A set of all matching words found in the document
        """
        # Create a new set() to store the matches
        matches = set()
        
        # Loop over all the indexes of the characters in the document (this value marks the start of the substring)
        for start_index in range(len(document)):
            # Keep track of your current level in the trie (a dictionary) starting at the root
            current_level = self.root
            
            # Use another nested loop to iterate over all the indexes of characters in the document, but start at the current index of the outer loop
            # (this value marks the potential end of the substring)
            for end_index in range(start_index, len(document)):
                char = document[end_index]
                
                # If the inner character is not in the current level, break out of the inner loop, there are no matches here
                if char not in current_level:
                    break
                
                # Otherwise, move to the next level in the trie (based on the inner character)
                current_level = current_level[char]
                
                # If the inner character's level contains the end symbol, add the substring to the matches set
                # You can calculate the full substring by slicing the document using the indexes of the outer and inner loops
                if self.end_symbol in current_level:
                    substring = document[start_index:end_index + 1]
                    matches.add(substring)
        
        # Return the set of matches
        return matches

    def advanced_find_matches(self, document, variations):
        """
        Finds all words from the trie that occur in the document, handling character variations.
        
        Args:
            document: The document string to search in
            variations: Dictionary mapping variation characters to their original characters
                       (e.g., {'@': 'a', '3': 'e'})
        
        Returns:
            A set of all matching words found in the document (with variations)
        """
        # Create a new set() to store the matches
        matches = set()
        
        # Loop over all the indexes of the characters in the document (this value marks the start of the substring)
        for start_index in range(len(document)):
            # Keep track of your current level in the trie (a dictionary) starting at the root
            current_level = self.root
            
            # Use another nested loop to iterate over all the indexes of characters in the document, but start at the current index of the outer loop
            # (this value marks the potential end of the substring)
            for end_index in range(start_index, len(document)):
                char = document[end_index]
                
                # If the character is in the variations dictionary, use the mapped original character
                # Otherwise, use the character as-is
                search_char = variations.get(char, char)
                
                # If the inner character (or its variation) is not in the current level, break out of the inner loop, there are no matches here
                if search_char not in current_level:
                    break
                
                # Otherwise, move to the next level in the trie (based on the inner character, using variation mapping)
                current_level = current_level[search_char]
                
                # If the inner character's level contains the end symbol, add the substring to the matches set
                # You can calculate the full substring by slicing the document using the indexes of the outer and inner loops
                # Note: We add the original substring (with variations), not the mapped version
                if self.end_symbol in current_level:
                    substring = document[start_index:end_index + 1]
                    matches.add(substring)
        
        # Return the set of matches
        return matches

    def longest_common_prefix(self):
        """
        Returns the longest common prefix among all words in the trie.
        
        Steps:
        1. Start at root
        2. Traverse as long as there's exactly one child (excluding end_symbol)
        3. Stop when we hit an end_symbol, multiple children, or no children
        """
        # Initialize a variable current that references the root of the trie
        current = self.root
        
        # Initialize a variable prefix to an empty string
        prefix = ""
        
        # Enter a forever while loop
        while True:
            # Get the "children" (keys) in the current dictionary
            children = list(current.keys())
            
            # If a child is an end_symbol, break the loop
            if self.end_symbol in children:
                break
            
            # Filter out end_symbol to get only character children
            char_children = [child for child in children if child != self.end_symbol]
            
            # If there is only one child, append the character to the prefix string and update the current dictionary to point to the child dictionary corresponding to the character
            if len(char_children) == 1:
                char = char_children[0]
                prefix += char
                current = current[char]
            # If there are multiple children or no children, break the loop
            else:
                break
        
        # Return the prefix string
        return prefix

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"
