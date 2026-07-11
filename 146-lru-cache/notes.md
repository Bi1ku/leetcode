Initial: `put` function is O(1) since it uses hashmaps. `get` function is O(n) since I loop thorugh the hashmap to find minimum value.

Optimal: Both are O(1) because insertions and deletions are handled by doubly linked list with points of leftmost and rightmost endpoints. Rightmost signifies latest, leftmost signifies oldest. Hash maps are used for constant constant lookups and point to the nodes in the doubly lists.

Concepts: Hash Maps, System Design, Nodes, Doubly Linked Lists
