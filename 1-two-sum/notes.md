### Initial:
- Brute force method using two loops
- Best case: O(1)
    - List like [2, 7, 8] with target of 9. Everything is at the front so the loop would only do one iteration.
- Worst case: O(n^2)
    - List like [8, 2, 7] with target of 9. The solution is at the back, so the loop would have to do n^2 iterations (keeping
    in mind the .index() function)
- Average case: O(n^2)
    - Typically we can expect to find the solution somewhere in the middle of the list, but this still simplifies to n^2 in Big O.

### Optimized:
- We can use a dictionary/hash map which has constant time look ups.
- Best case: O(1)
    - The solution is in the first two elements so constant speed.
- Worst cast: O(n)
    - We'll have to loop through every single array element. The last element is included in the solution. Traversing whole list
    and comparing with hashmap.
- Average case: O(n)
    - Typically expect to find solution somewhere in the middle of the list while looking up in hashmap. O(n/2) => O(n).

Main Concept: Hashmaps
