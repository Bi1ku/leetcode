Initial:
- Runtime is O(n + m) but could possibly be something worse like O(n^2 + m^2) becasuse of the numerous string
computations, mutations, and reversals. Also integer to string conversions.
- Convert linked list numbers to a string. Reverse those two strings. Convert to an integer. Add those integers
together. Convert the sum to a string. Reverse the string again. Make a linked list out of it and return.

Optimized:
- Runtime is O(max(n, m)) because it traverses through all the linkedin lists, whichever is larger and adds them together.
- It's useful that the linked lists are given in reverse because that's how we normally add.
    - Just make sure to carry the tens digit
- Go through each element of the linked list and add them together while keeping in mind the amount to carry over to the
next sum.
    - This should always happen until BOTH nodes hit a None.
    - You must always track the `carry` at the end.
