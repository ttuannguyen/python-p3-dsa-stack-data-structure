def reverse_string(string):
    stack = []

    for char in string: # O(n)
        stack.append(char)
    
    reversed = ""
    while stack:
        reversed += stack.pop() # O(n)

    return reversed 

# time complexity: O(2n), simplifying => O(n)
# print(reverse_string("hello"))


# method: non-stack, using while loop
def evaluate_keystrokes(string):
    i = len(string)-1
    result = ""
    skip = 0

    while i >=0:
        print(i, string[i])
        if string[i] == "<":
            skip +=1
            i -= 1
            # print("yes", "skip:", skip, "now i is:", i)
        else: 
            if skip > 0:
                # print("skip is now at", skip)
                i -= skip
                skip = 0
                # print("when there is skip:", "decrement i by skip of by skip # above", "then set skip to", skip)
                # print("string[i] is now at", string[i])
            else: 
                char = string[i]
                result = string[i] + result
                i -= 1
                # print("when there is no skip:", "add string[i]", char, "before the existing result to become", result)
    return result

print(evaluate_keystrokes('abcde<fg<h'))


