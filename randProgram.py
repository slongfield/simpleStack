"""rand_program generates random simpleStack programs, and evaulates them.

This is basically a really simple fuzzer for testing that no programs "go
wrong", where "go wrong" means "throw an exception".

Allows one exception to be thrown:
    MemoryError if the stack grows beyond 10,000 elements. These programs just
    tend to be randomly generated fork-bombs, which while technically valid,
    aren't interesting, and don't violate the spirit of simpleStack.

Assumess that a 100 line program will reach its final state in 10,000 steps,
which is a completely invalid assumption.
"""

import random
import string
import simpleStack

_DEBUG = False

_SYMBOLS = ["PRINT", "DUP", "INV", "--", "++", "SUB", "MOD", "SWP", "JNZ"]


def gen_program(min_size, max_size):
    """gen_program generates a random program."""
    size = random.randrange(min_size, max_size)
    prog = []
    for _ in range(size):
        # Randomly pick if we add a program symbol or random word.
        if random.choice([True, False]):
            prog.append(random.choice(_SYMBOLS))
        else:
            wordlen = random.randrange(0, 10)
            prog.append(''.join(random.choice(string.ascii_letters +
                                              string.digits) for _ in range(wordlen)))
    return prog

if __name__ == "__main__":
    # Generate 1000 programs, or 1 in debug mode
    mem_errors = 0
    num_runs = 1 if _DEBUG else 10000
    for _ in range(num_runs):
        prog = gen_program(10, 100)
        # Run for 100,000 steps. If in debug mode, actually print, otherwise,
        # don't.
        if _DEBUG:
            print("\n".join(prog))

        def fake_print(_, end=None):
            """Fake print that does nothing"""
            del end

        try:
            simpleStack.run_simple_stack(prog,
                                         max_steps=10000,
                                         printFun=print if _DEBUG else fake_print)
        except MemoryError:
            mem_errors += 1
    print("Ran {} runs, with {} memory errors".format(num_runs, mem_errors))
