# simpleStack

simpleStack is a very simple stack-base programming language written in Python.
There are no invalid simpleStack programs, though many of them do nothing of
interest.

This was written in response to a post on Paul Mandel's Facebook wall. All blame
goes to him.


## Examples:

I'm not sure if this language is Turing-complete. It might be. It implements all
of the important programs:

*  `hello.ss`: Hello World
*  `99bottle.ss`: 99 Bottles of Beer on the Wall
*  `fizzbuzz.ss`: Prints out Fizz if the number is divisible by 3, Buzz if its
   divisble by 5, and FizzBuzz if its divisible by 3 and 5.
*   `randProgram.py`: Generates a random program, and runs it to check and see
    if it ends up in some invalid state, or throws an error.

## Syntax:

Each line is treated as a symbol. This is not intended to be a super complete
set of the symbols you might need, they just happened to be the symbols I needed
to write all of the important programs above

 * `PRINT`: Pops the top element of the stack and prints it.
 * `DUP`  : Duplciates the current stack.
 * `INV`  : Pops off the head of the stack, inverts it, and pushes back on.
 * `--`   : Pops off the head of the stack, decrements it, and pushes back onto
            the stack.
 * `++`   : Pops off the head of the stack, increments it, and pushes back onto
            the stack.
 * `SUB`  : Pops the top two elements off the stack, subtracts and pushes back
            onto the stack.
 * `MOD`  : Pops the top two elements off the stack, and does modulo, and pushes
            it back onto the stack. Modulo zero returns None, to avoid division
            by zero.
 * `SWP`  : Pops two elements off the stack, swaps their order, and pushes back
            on.
 * `JNZ`  : Pops the top two elements off the stack, and if the top element was
            non-zero, jumps as far as the second element it popped.  If it would
            jump off the top of the program, it instead jumps to the top of the
            program.  If it jumps off the bottom of the program, the program
            ends.

If there's nothing in the stack, and a value needs to be popped, `None` will be
popped (see below for how types are handled).

If a line begins with '//' it's treated as a comment.

If a line contains something that isn't a defined part of the language, it's
pushed onto the stack to be used as data. This makes it slightly annoying to
print words that are part of the language, but this isn't a Quine language, so
who cares.

### Data types:
  * Integers, strings, and None, with lots of coersion to avoid type errors.
  * Integers and None are coerced to strings in the obvious way.
  * None is coerced to an integer as "0"
  * Strings:
     * Strings of digits are interpreted as those digits (e.g., `"-1"` is `-1`)
     * Empty string, or strings with no digits is treated as `0`
     * strings that contain characters have those characters stripped out before
      being interpreted by the above rules. for example, `2wenty thr3e` has all
      the characters removed to get `"23"`, which is interpreted as `23`.
      Might result in slightly unexpected errors if you attempt to use floating
      point numbers: `"1.3"` has the `'.'` stripped, and is interpreted as `"13"`.
