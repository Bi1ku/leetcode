- set is a hasmap without values
    - distinct keys only, if you attempt to add a nondistinct key... it just won't do anything
- cannot have lists as keys or inside sets because they are mutable
    - must convert into a tuple (which are immuateable after you create them, i.e., cannot add or remove elements)

to get a column from a 2-dimensional array, for i in grid[0]: column = [row[i] for row in grid]
