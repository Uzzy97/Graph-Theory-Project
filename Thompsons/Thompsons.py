# Thompson's Construction
# Usman Sattar
# G00345816

# Represents a state with two arrows, labelled by label.
# Use None for a label representing "e" arrows.
#Class called state
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
            accept = state()
            initial.edge1 = nfa1.initial
            initial.edge2 = nfa2.initial
            # Create a new accept state, connecting the accept states
            # of the two NFA's popped from the stack, to the new states.
            initial = state()
            nfa1.accept.edge1 = accept
            nfa2.accept.edge1 = accept
            # Push new NFA to the stack
            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)
        elif c == '*':
            # Pop a single NFA from the stack.
            nfa1 = nfastack.pop()
            initial, accept = state(), state()
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
            nfastack.append(nfa(initial, accept))
    # nfastack should only have a single nfa on it at this point.
    return nfastack.pop()
#Tests
print(compile("ab.cd.|"))
print(compile("aa.*"))