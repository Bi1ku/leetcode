nums[left], nums[right] = nums[right], nums[left] # skips the need for a temp variable
    - Python builds temporary tuples under the hood

- When right pointer reaches zero, skip and do nothing
- Left pointer will always be on the leftmost zero
- Swap when values when right pointer reaches a number, then increment left by one
