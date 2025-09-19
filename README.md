# Binary Search Tree in Python

This project implements a Binary Search Tree (BST) in Python with basic operations:
- Insert values (`append`)
- Remove values (`remove_value`)
- Traversals (pre-order, in-order, post-order)
- Search for values
- Get minimum and maximum values
- Change a node's value

## Example Usage

```python
from tree import Tree

# Create tree and insert values
test = Tree()
test.append(5)
test.append(8)
test.append(6)
test.append(9)
test.append(3)
test.append(4)
test.append(2)

# Remove values
test.remove_value(5)   # Removes root
test.remove_value(30)  # Does nothing, value not found

# Print in-order traversal (left, root, right)
test.print_in_order()

# Print pre-order traversal (root, left, right)
test.print_pre_order()

# Print post-order traversal (left, right, root)
test.print_post_order()
