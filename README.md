# Binary Search Tree in Python

This project implements a Binary Search Tree (BST) in Python with basic operations:  
- Insert values (`append`)  
- Remove values (`remove_value`)  
- Traversals (pre-order, in-order, post-order)  
- Search for values  
- Get minimum and maximum values  
- Change a node's value  

---

## 🐍 1. Basic Usage (easiest way)

If you just want to try the tree without installing anything, copy **`tree.py`** into the same folder as your project and use:

```python
from tree import Tree

tree = Tree()
tree.append(5)
tree.append(3)
tree.append(7)
tree.print_in_order()
```

---

## 📦 2. Advanced Usage (install as a package)

If you want to use this as a Python package, you first need **Git installed**.  
👉 [Download Git](https://git-scm.com/downloads) if you don’t already have it.

Then install directly from GitHub using pip:

```bash
pip install git+https://github.com/Ahmedhm1/BST---Binary-Search-Tree-Data-Structure.git
```

Now you can import it anywhere:

```python
from bst import Tree

tree = Tree()
tree.append(10)
tree.append(4)
tree.append(12)
tree.print_in_order()
```

---

## 🔎 Example Usage

```python
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
```

---

## 📂 Project Structure
```
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
```

---

## 📖 Source Code
➡️ [View `tree.py`](./bst/tree.py) directly if you just want to read the implementation.
