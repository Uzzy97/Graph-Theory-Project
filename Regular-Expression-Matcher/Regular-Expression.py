# Regular Expression Matcher
# Usman Sattar
# G00345816

def shunt(infix):
    """The Shunting Yard Algorithm for converting infix regular expressions to postfix"""

    # Special characters for regular expressions and thir precedence.
    specials = {'*': 50, '.': 40, '|': 30}

    # Will eventually be the output
    postfix = ""
    # Operator stack
    stack = ""

    # Loop through the string a character at a time
    for c in infix:
        # If an open bracket, push to the stack
        if c == '(':
            stack = stack + c
        # If a closing bracket, pop form stack, push to output until open bracket
        elif c == ')':
            while stack[-1] != '(':
                postfix, stack = postfix + stack[-1], stack[:-1]
            stack = stack[:-1]
        # If it's an operator, push to stack after popping lower or equal precedence
        # operators from top of stack into output.
        elif c in specials:
            while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
                postfix, stack = postfix + stack[-1], stack[:-1]
            stack = stack + c
        # Regular characters are pushed immediatly to the output.
        else:
            postfix = postfix + c
    
    # Pop all remaining operators from stack to output.
    while stack:
        postfix, stack = postfix + stack[:-1], stack[:-1]

    # Return postfix regex
    return postfix


# Represents a state with two arrows, labelled by label.
# Use None for a label representing "e" arrows.

class state:
    # Variables with no values yet
    label = None
    edge1 = None
    edge2 = None

# An NFA is represented by its initial and accept states.
class nfa:
    initial = None
    accept = None

    # Constructor
    def __init__(self, initial, accept):
        self.initial = initial
        self.accept = accept
# Regualar expression compiler that we are compiling
# From text to data
def compile(postfix):
    """Compiles a postfix regular expression into an NFA"""

    nfastack = []

    for c in postfix:
        if c == '.':
            # Pop two NFA's off the stack.
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()
            # Connect first NFA's accept state to the second's initial
            nfa1.accept.edge1 = nfa2.initial
            # Push NFA to the stack.
            newnfa = nfa(nfa1.initial, nfa2.accept)
            nfastack.append(newnfa)
        elif c == '|':
            # Pop two NFA's off the stack.
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()
            # Create a new initial state, connect it to initial states
            # of the two NFA's popped from the stack.
            initial = state()
            initial.edge1 = nfa1.initial
            initial.edge2 = nfa2.initial
            # Create a new accept state, connecting the accept states
            # of the two NFA's popped from the stack, to the new states.
            accept = state()
            nfa1.accept.edge1 = accept
            nfa2.accept.edge1 = accept
            # Push new NFA to the stack
            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)
        elif c == '*':
            # Pop a single NFA from the stack.
            nfa1 = nfastack.pop()
            # Create new initial and accept states
            initial = state()
            accept = state()
            # Join the new initial state to nfa1's initial state and the new accept state.
            initial.edge1 = nfa.initial
            initial.edge2 = accept
            # Join the old accept state to the new accept state and nfa's initial state.
            nfa1.accept.edge1 = nfa.initial
            nfa1.accept.edge2 = accept
            # Push new NFA to the stack.
            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)
        else:
            # Create new initial and accept states.
            accept = state()
            initial = state()
            # Join the initial state and the accept state using an arrow labelled c.
            initial.label = c
            initial.edge1 = accept
            # Push the new NFA to the stack.
            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)

    # nfastack should only have a single nfa on it at this point.
    return nfastack.pop()

def followees(state):
    """Return set of states that can be reached from state following e arrows"""
    # Create a new set, with state as its only member
    states = set()
    states.add(state)

    # Check if state has arrowa labelled e from it
    if state.label is None:
        # Check if edge1 is a state
        if state.edge1 is not None:
            # If there is an edge1, follow it
            # |= union
            states |= followees(state.edge1)
        # Check is edge2 to is a state
        if state.edge2 is not None:
            # If there is an edge2, follow it
            states |= followees(state.edge2)

    # Return the set of states
    return states


def match(infix, string):
    """Matches string to infix regular expression"""

    # Shunt and compile the regular expression
    postfix = shunt(infix)
    nfa = compile(postfix)

    # The current set of states and the next set of states
    current = set()
    next = set()

    # Add the initial state to the current set
    current |= followees(nfa.initial)

    # Loop through each char in the string
    for s in string:
        # Loop through the current set of states
        for c in current:
            # Check if that state is labelled s
            if c.label == s:
                # Add the edge1 state to the next set
                next |= followees(c.edge1)
        # Set current to next and clear out next
        current = next
        next = set()

    # Check if the accept state is in the set of current states
    return (nfa.accept in current)


# Few Tests
infixes = ["a.b.c", "a.(b|d).c*", "(a.(b|d))*", "a.(b.b)*.c"]
# Strings matching infixes
strings = ["", "abc", "abbc", "abcc", "abad", "abbbc"]

for i in infixes:
    for s in strings:
        print(match(i, s), i, s)