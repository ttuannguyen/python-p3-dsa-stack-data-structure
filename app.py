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
# apprach: iterating thru the string from back to front 
# use placeholder var of skip to keep track of how many times we need to backspace by skipping over characters
def evaluate_keystrokes(string):
    i = len(string)-1
    result = ""
    skip = 0

    while i >=0:
        # print(i, string[i])
        if string[i] == "<":
            skip +=1
            i -= 1
            # print("yes", "skip:", skip, "now i is:", i)
        else: 
            if skip > 0:
                # print("skip is now at", skip)
                i -= skip
                skip = 0
                # print("when there is skip:", "decrement i by skip # above to move to the appropriate next character", "then set skip to", skip)
                # print("string[i] is now at", string[i])
            else: 
                # char = string[i]
                result = string[i] + result
                i -= 1
                # print("when there is no skip:", "simply add the current character string[i]", char, "before the existing result to become", result)
    return result
# print(evaluate_keystrokes('abcde<fg<h'))

# method: stack 
# approach: every time we encounter <, we pop it off the stack 
def  evaluate_keystrokes_using_stack(string):
    stack = []
    for char in string:
        if char == "<":
            # every time we encounter <, we pop it off the stack when the stack is not empty
            if len(stack) != 0: # check for an empty stack in case < is the first character in the stack 
                stack.pop()
        else:
            stack.append(char)
        print("char:", char, "stack:", stack)
    
    result = ""
    while stack:
        # by the end, all the characters that don't get erased remain in the stack 
        # so we simply pop them off and add them to the result string
        result = stack.pop() + result
        print("result:", result)
    return result

evaluate_keystrokes_using_stack('abcde<fg<h')


