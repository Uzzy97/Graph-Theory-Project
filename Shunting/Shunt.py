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

    for c in infix:
        if c == '(':
            stack = stack + c
        elif c == ')':
            while stack[-1] != '(':
                postfix, stack = postfix + stack[-1], stack[:-1]
            stack = stack[:-1]
        elif c in specials:
            # While stack is not the empty string
            # Looking for C in specials dictionary, if not there give value 0 instead
            while stack and specials.get(c,0) <= specials.get(stack[-1],0):
                postfix,stack = postfix + stack[-1], stack[:-1]
            stack = stack + c
        else:
            postfix = postfix + c 

    while stack:
        postfix, stack = postfix + stack[-1], stack[:-1]

    # Returning postfix     
    return postfix

print(shunt("(a.b)|(c*.d)"))