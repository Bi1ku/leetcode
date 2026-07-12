Initial Solution:
- Average runtime is O(n) because you're traversing through the linked list.
    - This runtime already optimal.
- Average memory is O(n) because you're adding each node of the liset to a hashset.
    - We want to get our memory to O(1).

Concepts: Floyd's Tortoise and Hare Algorithm

Optimal Solution:
- Average runtime is still O(n), you can't get around traversing through the linked list.
- Memory is now O(1) because you're storing two constant variables the slow tortoise and the fast hare.

- The slow iterable will always intersect with the fast interable if it loops.
- The fast iterable will always reach None first if it doesn't loop.
- This prevents us from having to use a hashset which is very memory intensive.
