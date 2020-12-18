+ [Maximum Depth of Binary Tree](#maximum-depth-of-binary-tree)
+ [Binary Tree Inorder Traversal](#binary-tree-inorder-traversal)
+ [Invert Binary Tree](#invert-binary-tree)
+ [Binary Search Tree Iterator](#binary-search-tree-iterator)
+ [Binary Tree Level Order Traversal](#binary-tree-level-order-traversal)
+ [Kth Smallest Element in a BST](#kth-smallest-element-in-a-bst)
+ [Validate Binary Search Tree](#validate-binary-search-tree)
+ [Symmetric Tree](#symmetric-tree)
<!-----solution----->

## Symmetric Tree

https://leetcode.com/problems/symmetric-tree/

```python
def isSymmetric(self, root: TreeNode) -> bool:
    if not root:
        return True

    return self.isMirror(root.left, root.right)

def isMirror(self, left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False

    if left.val == right.val:
        innerPair = self.isMirror(left.left, right.right)
        outerPair = self.isMirror(left.right, right.left)
        return innerPair and outerPair
    else:
        return False
```

## Validate Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree/

```python
def isValidBST(self, root: TreeNode) -> bool:
    traversed = self.inorder(root)
    if len(traversed) == len(set(traversed)):
        return traversed == sorted(traversed)
    else:
        return False

def inorder(self, root):
    if root != None:
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
    else:
        return []
```

## Kth Smallest Element in a BST

https://leetcode.com/problems/kth-smallest-element-in-a-bst/

```python
def kthSmallest(self, root: TreeNode, k: int) -> int:
    self.kCount = 0
    def inOrder(node):
        if node is None:
            return None
        newNode = inOrder(node.left)
        if newNode is not None:
            return newNode
        self.kCount += 1
        if self.kCount == k:
            return node.val
        return inOrder(node.right)
    return inOrder(root)
```

## Binary Tree Level Order Traversal

https://leetcode.com/problems/binary-tree-level-order-traversal/

```python
def levelOrder(self, root: TreeNode) -> List[List[int]]:
    dict = {}
    if not root:
        return []
    q = []
    q.append([root, 0])
    while len(q) != 0:
        curr = q.pop(0)
        if curr[1] not in dict:
            dict[curr[1]] = [curr[0].val]
        else:
            temp = dict[curr[1]] + [curr[0].val]
            dict[curr[1]] = temp
        if curr[0].left != None:
            q.append([curr[0].left, curr[1]+1])
        if curr[0].right != None:
            q.append([curr[0].right, curr[1]+1])
    out = []
    for layer in dict.values():
        out.append(layer)
    return out
```

## Binary Search Tree Iterator

https://leetcode.com/problems/binary-search-tree-iterator/

```python
def __init__(self, root: TreeNode):
    self.ordered = []

    def traverse(node):
        if node:
            traverse(node.left)
            self.ordered.append(node.val)
            traverse(node.right)

    traverse(root)
    self.curr_index = -1

def next(self) -> int:
    self.curr_index += 1
    if self.curr_index < len(self.ordered):
        return self.ordered[self.curr_index]
    else:
        return None

def hasNext(self) -> bool:
    return self.curr_index+1 < len(self.ordered)
```

## Invert Binary Tree

https://leetcode.com/problems/invert-binary-tree/

```python
def invertTree(self, root: TreeNode) -> TreeNode:
    if not root:
        return None

    root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    return root
```

## Binary Tree Inorder Traversal

https://leetcode.com/problems/binary-tree-inorder-traversal/

```python
def inorderTraversal(self, root: TreeNode) -> List[int]:
    if root is None:
        return []
    return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
```

## Maximum Depth of Binary Tree

https://leetcode.com/problems/maximum-depth-of-binary-tree/

```python
def maxDepth(self, root: TreeNode) -> int:
    if root is None:
        return 0
    return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)
```