# Preorder Traversal - Beginner's Guide

## What is Preorder Traversal?

**Preorder** means "visit the node BEFORE its children." It's like visiting a tree from top to bottom, left to right, but always saying "hello" to the parent before exploring its children.

## The Pattern: ROOT → LEFT → RIGHT

Think of it like reading a book:
1. **Read the chapter title** (the current node) ✅
2. **Read the left section** (left child)
3. **Read the right section** (right child)

## Step-by-Step Logic

```python
def preorder(self, visited):
    # Step 1: Visit current node FIRST (if it has a value)
    if self.val is not None:
        visited.append(self.val)
    
    # Step 2: Then explore LEFT subtree
    if self.left is not None:
        self.left.preorder(visited)
    
    # Step 3: Then explore RIGHT subtree
    if self.right is not None:
        self.right.preorder(visited)
    
    # Step 4: Return the list we've been building
    return visited
```

## Example Walkthrough

Let's trace through this tree:
```
        4
      /   \
     2     7
    /     /
   1     6
```

### Execution Flow:

1. **Start at node 4**
   - ✅ Visit 4 → `visited = [4]`
   - Go to left child (2)

2. **At node 2**
   - ✅ Visit 2 → `visited = [4, 2]`
   - Go to left child (1)

3. **At node 1**
   - ✅ Visit 1 → `visited = [4, 2, 1]`
   - No left child, done
   - No right child, done
   - Return to node 2

4. **Back at node 2**
   - Left subtree done
   - No right child, done
   - Return to node 4

5. **Back at node 4**
   - Left subtree done
   - Go to right child (7)

6. **At node 7**
   - ✅ Visit 7 → `visited = [4, 2, 1, 7]`
   - Go to left child (6)

7. **At node 6**
   - ✅ Visit 6 → `visited = [4, 2, 1, 7, 6]`
   - No left child, done
   - No right child, done
   - Return to node 7

8. **Back at node 7**
   - Left subtree done
   - No right child, done
   - Return to node 4

9. **Back at node 4**
   - Right subtree done
   - Return final result: `[4, 2, 1, 7, 6]`

## Key Concepts

### 1. **Recursion**
The method calls itself! When we do `self.left.preorder(visited)`, we're saying:
- "Hey left child, do your own preorder traversal"
- The same `visited` list is passed around and modified

### 2. **Same List, Shared Reference**
Notice we pass the same `visited` list to all recursive calls. Python lists are mutable, so:
- All recursive calls add to the SAME list
- No need to merge results - they automatically accumulate

### 3. **Order Matters: Root First!**
- **Preorder**: Visit node → left → right
- **Inorder**: Left → visit node → right  
- **Postorder**: Left → right → visit node

"Pre" means "before" - we visit the node BEFORE its children!

## Visual Representation

```
Visit order: 4 → 2 → 1 → 7 → 6
            ↑   ↑   ↑   ↑   ↑
            │   │   │   │   │
         [ROOT][ROOT][LEAF][ROOT][LEAF]
            │   │
            │   └─ LEFT of 4
            └───── START HERE
```

## Edge Cases

1. **Empty node** (`self.val is None`)
   - Skip adding to list
   - But still check children (if any)

2. **No left child** (`self.left is None`)
   - Skip left traversal
   - Move to right

3. **No right child** (`self.right is None`)
   - Skip right traversal
   - Return visited list

4. **Leaf node** (no children)
   - Just add value and return
   - `visited.append(self.val)` → done!

## Why Use Preorder?

- **Creating backups**: Visit nodes in a predictable order
- **Printing tree structure**: Get parent before children
- **Copying trees**: Rebuild tree in same structure
- **Prefix expressions**: Useful for expression trees

## Memory Tip

Think: **"Parent, then kids"**
- Parent first (current node)
- Then left kid
- Then right kid

That's preorder! 🎯

