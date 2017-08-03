"""simpleStack.py implements a very simple stack-based language.

This language has no invalid programs.

I'm not sure if it's Turing-complete, but it can implement all important
programs: Hello World, 99 Bottles of Beer, and FizzBuzz.
"""

import sys

_DEBUG = False

# For execution sake, die if the stack gets too large.
_MAX_STACK = 10000


class Stack(object):
    """Stack is slightly modified from a default list stack.

    If you pop from it when it's empty, it will return None, instead of throwing
    an IndexError
    """

    def __init__(self):
        self.stack = []

    def push(self, elem):
        """Push pushes onto the stack."""
        if len(self.stack) > _MAX_STACK:
            raise MemoryError("Stack overflow!")
        self.stack.append(elem)

    def pop(self):
        """Pop pops from the stack. Returns None if the stack is empty."""
        if self.stack:
            return self.stack.pop()

    def dup(self):
        """Appends a copy of the stack to itself"""
        if len(self.stack) > _MAX_STACK:
            raise MemoryError("Stack overflow!")
        self.stack.extend(self.stack)


def coerce_to_int(val):
    """coerce_to_int coerces a value to an integer."""
    if isinstance(val, int):
        return val
    if val is None:
        return 0
    # Otherwise, val must be a string, since that's the only other kind of data
    # type that we can create. Strip out all non-digit characters.
    new_val = "".join([c for c in val if c in map(str, list(range(10)))])
    if new_val == "":
        return 0
    return int(new_val)


def decrement(val):
    """decrement coerces a value to an integer, and then decrements."""
    return coerce_to_int(val) - 1


def increment(val):
    """decrement coerces a value to an integer, and then decrements."""
    return coerce_to_int(val) + 1


def invert(val):
    """Negates the value at the top of the stack."""
    return -1 * coerce_to_int(val)


def modulo(val1, val2):
    """Returns val1 % val2. Returns None if val2 acts like zero."""
    if coerce_to_int(val2) == 0:
        return None
    return coerce_to_int(val1) % coerce_to_int(val2)


def sub(val1, val2):
    """Returns val1 - val2."""
    return coerce_to_int(val1) - coerce_to_int(val2)


def run_simple_stack(lines, max_steps=None, printFun=print):
    """run_simple_stack runs a simple stack program.

    Args:
        lines: [list of strings]: The simpleStack program
    """
    stack = Stack()
    i = 0
    step = 0
    while i < len(lines):
        line = lines[i]
        i += 1
        step += 1
        if _DEBUG:
            print("Executing", line, "with stack", stack.stack, "at step", step)
            input()
        if max_steps and step > max_steps:
            break
        if line.startswith("//"):
            continue
        line = line.strip('\n').replace("\\n", "\n")
        if line == "PRINT":
            printFun(stack.pop(), end="")
        elif line == "--":
            stack.push(decrement(stack.pop()))
        elif line == "++":
            stack.push(increment(stack.pop()))
        elif line == "INV":
            stack.push(invert(stack.pop()))
        elif line == "SUB":
            stack.push(sub(stack.pop(), stack.pop()))
        elif line == "MOD":
            stack.push(modulo(stack.pop(), stack.pop()))
        elif line == "DUP":
            stack.dup()
        elif line == "SWP":
            fst = stack.pop()
            snd = stack.pop()
            stack.push(fst)
            stack.push(snd)
        elif line == "JNZ":
            cond = stack.pop()
            dist = coerce_to_int(stack.pop())
            if cond:
                i += dist
            if i < 0:
                i = 0
        else:
            stack.push(line)

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        run_simple_stack(f.readlines())
