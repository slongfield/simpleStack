// Implementation of Wolfram's (2,3) Turing machine.
// Sure, not everyone agrees that it's universal, but it seems like enough
// people do, and it's similiar enough to more widely agreed-to-be universal
// Turing machines that this code could be generalized if some pedant needed
// satisfaction.
0
0
HEAP
DUP
48
SWP
// State was 0 maps to A, 1 maps to B, so JNZ here goes to line 60 if the state is B
JNZ
GET
14
MUL
++
1
JNZ
// First handle the case where we're in state A, and the current value is 0:
// P1 R B
++
SWP
DUP
PUT
++
SWP
24
INV
1
JNZ


// Next, the case where we're in state A, and the current value is 1:  P2 L A
SWP
DUP
SWP
++
++
SWP
PUT
--
SWP
40
INV
1
JNZ
// Last for A, state is A, current value is 2: P1, L, A
SWP
DUP
SWP
++
SWP
PUT
--
SWP
53
INV
1
JNZ
// Handle the case where the current state is B
GET
15
MUL
++
1
JNZ
// State is B, value is 0 -- P2 L A
--
SWP
DUP
SWP
++
++
SWP
PUT
--
SWP
75
INV
1
JNZ
// State is B, value is 1 -- P2, R, B
SWP
DUP
SWP
++
SWP
PUT
++
SWP
88
INV
1
JNZ


// State is B, value is 2 -- P0, R, A
--
SWP
DUP
PUT
++
SWP
101
INV
1
JNZ
