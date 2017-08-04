// fizzbuzz.ss prints out a FizzBuzz answer
1
DUP
// Check for mod 15
15
SWP
MOD
5
SWP
JNZ
FizzBuzz\n
PRINT
32
1
JNZ
// Check for mod 5
DUP
5
SWP
MOD
5
SWP
JNZ
Buzz\n
PRINT
19
1
JNZ
// Check for mod 3
DUP
3
SWP
MOD
5
SWP
JNZ
Fizz\n
PRINT
6
1
JNZ
// Print out if we didn't print earler
DUP
PRINT
\n
PRINT
// Increment, and if we're not at 100, jump back to the top
DUP
++
SWP
100
SWP
SUB
55
INV
SWP
JNZ
