### Approach:
#1. Convert the given string into a list using `list()` because strings are immutable.
#2. Lists are mutable, so we can modify individual characters.
#3. Use `l[position] = character` to replace the character at the given index.
#4. Use `''.join(l)` to combine all list elements into a single string.
#5. Return the modified string using `return`.

def mutate_string(string, position, character):
    l = list(string)
    l[5]= character
    
    return ''.join(l)
