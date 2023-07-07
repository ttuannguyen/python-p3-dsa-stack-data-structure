def reverse_string(string):
    stack = []

    for char in string: # O(n)
        stack.append(char)
    
    reversed = ""
    while stack:
        reversed += stack.pop() # O(n)

    return reversed 

# time complexity: O(2n), simplifying => O(n)
print(reverse_string("hello"))
