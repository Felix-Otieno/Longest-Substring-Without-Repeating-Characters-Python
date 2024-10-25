def longest_substring(text):
    """
    A function that finds the longest substring without repeating characters in the string.
    Passed parameter called text that is the string to be checked and return that dispaly the highest length of the unique characters in the string.

    """
    unique_chars = set() # Set to store unique characters of the current substring
    first_index = 0 # Start index of the current substring
    highest_length = 0 # Variable to store the highest length of a unique substring found
    
    for i in range(len(text)): # Loop through each character in the string by index
        while text[i] in unique_chars: # Check if the current character present in the set ajust the starting index  

            unique_chars.remove(text[first_index]) # Remove the character at the current start index from the set 
            first_index += 1 # Increment the start index to maintain unique substring

        unique_chars.add(text[i]) # Add the current character to the set
        highest_length = max(highest_length, i - first_index + 1) # Update the maximum length if the current substring is longer

    return highest_length # Return the length of the set

text = "xyzxyzyy" # Variable that store the string of the characters to be found in the substring
print(longest_substring(text)) # Display output 
