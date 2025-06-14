from phithon import *

# 1. Initialization and Append
print("1. Initialization and Append")
my_list = list([5, 1, 4])
my_list.append(2)
my_list.append(3)
print(f"  Initial list: {[item for item in my_list]}")

# 2. Indexing (1-based)
print("\n2. Indexing (1-based)")
print(f"  Item at index 1: {my_list[1]}") # Should be 5
print(f"  Index of value 4: {my_list.index(4)}") # Should be 3

# 3. Pop
print("\n3. Pop")
popped_item = my_list.pop(2) # Pop item at index 2 (value 1)
print(f"  Popped item at index 2: {popped_item}")
print(f"  List after pop: {[item for item in my_list]}")

# 4. Insert
print("\n4. Insert")
my_list.insert(2, 99) # Insert 99 at index 2
print(f"  List after inserting 99 at index 2: {[item for item in my_list]}")

# 5. Remove
print("\n5. Remove")
my_list.remove(5) # Remove first occurrence of 5
print(f"  List after removing 5: {[item for item in my_list]}")

# 6. Count
print("\n6. Count")
print(f"  Count of value 3: {my_list.count(3)}")

# 7. Sort
print("\n7. Sort")
my_list.sort()
print(f"  Sorted list: {[item for item in my_list]}")

# 8. Reverse
print("\n8. Reverse")
my_list.reverse()
print(f"  Reversed list: {[item for item in my_list]}")

# 9. Copy and Clear
print("\n9. Copy and Clear")
list_copy = my_list.copy()
my_list.clear()
print(f"  Original list after clear: {[item for item in my_list]}")
print(f"  Copied list: {[item for item in list_copy]}")

# 10. pyrange
print("\n10. pyrange")
# Note: my_list was cleared in step 9. We'll use the copy.
print(f"  Iterating from 1 to 4 over the copied list: {[item for item in list_copy]}")
for i in range(4):
    print(f"  Item at index {i}: {list_copy[i]}")

# 11. Advanced pyrange features
print("\n11. Advanced pyrange features")
r = range(1, 11, 2)  # Should be 1, 3, 5, 7, 9
print(f"  pyrange(1, 11, 2): {r}")
print(f"  Length of r: {len(r)}")
print(f"  Element at index 3: {r[3]}") # Should be 5
print(f"  Element at index -1: {r[-1]}") # Should be 9
print(f"  Is 5 in r? {5 in r}")
print(f"  Is 6 in r? {6 in r}")
print("  Iterating through r:")
for num in r:
    print(f"    {num}")

# 12. Single-argument pyrange
print("\n12. Single-argument pyrange")
r_simple = range(8) # Should be 1, 2, 3, 4, 5, 6, 7, 8
print(f"  pyrange(8): {r_simple}")
print(f"  Length of r_simple: {len(r_simple)}")
print(f"  Last element: {r_simple[-1]}")
print("  Iterating through r_simple:")
for num in r_simple:
    print(f"    {num}")