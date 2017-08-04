# simpleStack

simpleStack is a very simple Turing-complete stack-based programming language
written in Python.

This language was not designed to be pretty, or easy to write. It was designed
to be a Turing-complete language in which any combination of valid symbols
yields a runnable program that was higher level than machine code.

This was written in response to a post on Paul Mandel's Facebook wall. All blame
goes to him.


## Examples:

To show the syntax of the language, and to demonstrate that it can be used for
something (somewhat) useful, there are a few programs under the `examples`
directory:

*  `hello.ss`: Prints "Hello World!"
*  `99bottles.ss`: Prints the "99 Bottles of Beer on the Wall" song
*  `fizzbuzz.ss`: Prints out Fizz if the number is divisible by 3, Buzz if its
   divisible by 5, and FizzBuzz if its divisible by 3 and 5.
*  `turing.ss`: Wolfram's (2,3) [Turing
   machine](https://en.wikipedia.org/wiki/Wolfram%27s_2-state_3-symbol_Turing_machine).
    This example proves that the language is turing complete.

Run each of these programs with

```shell
./simpleStack.py examples/[program]
```

If you enable debug mode by setting `_DEBUG` to true, you can trace the state of
execution, as well as the stack and heap.

I also provide a random program generator, `randProgram.py`, which generates a
random program, and runs it to check and see if it ends up in some invalid
state or throws an error. It runs by its own, and tests that any random
combination of symbols is a runnable simpleStack program.

## Syntax/Semantics:

Each line of the program is treated as a symbol. This is not intended to be a
super complete set of the symbols you might need, they just happened to be the
symbols I needed to write all of the important programs above.

 * `PRINT`: Pops the top element of the stack and prints it.
 * `DUP`  : Duplicates the current stack.
 * `INV`  : Pops off the head of the stack, inverts it, and pushes back on.
 * `--`   : Pops off the head of the stack, decrements it, and pushes back onto
            the stack.
 * `++`   : Pops off the head of the stack, increments it, and pushes back onto
            the stack.
 * `SUB`  : Pops the top two elements off the stack, subtracts and pushes back
            onto the stack.
 * `MUL`  : Pops the top two elements off the stack, multiplies, and pushes.
 * `MOD`  : Pops the top two elements off the stack, and does modulo, and pushes
            it back onto the stack. Modulo zero returns None, to avoid division
            by zero.
 * `SWP`  : Pops two elements off the stack, swaps their order, and pushes back
            on.
 * `JNZ`  : Pops the top two elements off the stack, and if the top element was
            non-zero, jumps as far as the second element it popped. All jumps
            are relative. If it would jump off the top of the program, it
            instead jumps to the top of the program. If it jumps off the bottom
            of the program, the program ends.

If there's nothing in the stack, and a value needs to be popped, `None` will be
popped (see below for how types are handled).

Along with the stack, there are two instructions that allow you to work with a
heap, which is implemented as a Python dictionary. Addresses into the heap are
coerced into integers, and there is no memory management. Reading from
uninitialized memory returns `None`.

 * `PUT`  : Pops two elements off the stack, uses the first as an address to
            store the second in the heap.
 * `GET`  : Pops an element off the stack, and uses that as an address to pull
            data from the heap, which is in turn pushed onto the stack.

If a line begins with '//' it's treated as a comment.

If a line contains something that isn't a defined part of the language, it's
pushed onto the stack to be used as data. This makes it slightly annoying to
print words that are part of the language, but this isn't a Quine language, so
who cares.

### Data types:
  * Integers, strings, and None, with lots of coercion to avoid the possibility
    of type errors.
  * Integers and None are coerced to strings in the obvious way.
  * None is coerced to an integer as "0"
  * Strings:
     * Strings of digits are interpreted as those digits (e.g., `"10"` is `10`)
     * Empty string, or strings with no digits is treated as `0`
     * strings that contain characters have those characters stripped out before
      being interpreted by the above rules. for example, `2wenty thr3e` has all
      the characters removed to get `"23"`, which is interpreted as `23`.
      Might result in slightly unexpected errors if you attempt to use floating
      point numbers: `"1.3"` has the `'.'` stripped, and is interpreted as `"13"`.
