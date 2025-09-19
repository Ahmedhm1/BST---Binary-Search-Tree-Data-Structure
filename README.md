Binary Search Tree in Python

This project implements a Binary Search Tree (BST) in Python with basic operations:

Insert values (append)

Remove values (remove_value)

Traversals (pre-order, in-order, post-order)

Search for values

Get minimum and maximum values

Change a node's value

📦 Installation / Usage
1. As a package (recommended)

Clone the repo and install in editable mode:

git clone https://github.com/Ahmedhm1/BST---Binary-Search-Tree-Data-Structure.git
cd BST---Binary-Search-Tree-Data-Structure
pip install -e .


Then in your Python code:

from bst.tree import Tree

tree = Tree()
tree.append(5)
tree.append(3)
tree.append(7)
tree.print_in_order()




2. Basic usage (just tree.py)

If you don’t want to install anything, just copy tree.py into your project folder and use:

from tree import Tree

tree = Tree()
tree.append(5)
tree.append(3)
tree.append(7)
tree.print_in_order()

🔎 Example Usage
from bst import Tree

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

📂 Project Structure
BST---Binary-Search-Tree-Data-Structure/
│
├── bst/              # Package source code
│   ├── __init__.py   # Exports Tree
│   └── tree.py       # Binary Search Tree implementation
│
├── test.py           # Example test file
├── setup.py          # Package setup script
├── pyproject.toml    # (Optional) modern build file
└── README.md

📖 Source Code

➡️ View tree.py
 directly if you just want to read the implementation.
