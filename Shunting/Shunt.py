# Usman Sattar
# G00345816
# Shunting Yard Algorithm

# Defining A Function
def shunt(infix):
    # Specials from dictionary and value 
    specials = {'*': 50, '.': 40, '|': 30}
    # Two blank strings
    postfix = ""
    stack = ""
    # Loop through the string, character at a time
    for c in infix:
        # Open bracket = push to the stack
        if c == '(':
            stack = stack + c
        # Closing bracket = pop form stack, push to output until open bracket
        elif c == ')':
            while stack[-1] != '(':
                postfix, stack = postfix + stack[-1], stack[:-1]
            stack = stack[:-1]
        # Operator = push to stack after popping lower or equal precedence
        # operators from top of stack into output.
        elif c in specials:
            # While stack is not the empty string
            # Looking for C in specials dictionary, if not there give value 0 instead
            while stack and specials.get(c,0) <= specials.get(stack[-1],0):
                postfix,stack = postfix + stack[-1], stack[:-1]
            stack = stack + c
        # Regular characters are pushed immediatly to the output.
        else:
            postfix = postfix + c 
    # Pop all remaining operators from stack to output.
    while stack:
        postfix, stack = postfix + stack[-1], stack[:-1]

    # Returning postfix     
    return postfix
# Tests
print(shunt("(a.b)|(c*.d)"))