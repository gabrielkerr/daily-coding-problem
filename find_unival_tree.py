"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    
def find_num_unival_trees(n):

    # If node is a leaf, return 1
    if n.left == None and n.right == None:
        return (1, True)

    # If both nodes are not null
    if n.left != None and n.right != None:
        num_trees = 0
        num_trees_left, diff_tree_left = find_num_unival_trees(n.left)
        num_trees_right, diff_tree_right = find_num_unival_trees(n.right)

        if n.val == n.left.val and n.val == n.right.val and diff_tree_left and diff_tree_right:
            num_trees = 1 + num_trees_left + num_trees_right
            return (num_trees, True)

        return (num_trees_left + num_trees_right, False)

    # If left node is not null
    if n.left != None: 
        num_trees = 0
        num_trees_left, diff_tree_left = find_num_unival_trees(n.left)

        if n.val == n.left.val and diff_tree_left:
            num_trees = 1 + num_trees_left 
            return (num_trees, True)

        return (num_trees_left, False)

    # If right node is not null
    if n.right != None: 
        num_trees = 0
        num_trees_right, diff_tree_right = find_num_unival_trees(n.right)

        if n.val == n.right.val and diff_tree_right:
            num_trees = 1 + num_trees_right
            return (num_trees, True)

        return (num_trees_right, False)



if __name__ == '__main__':
    n = Node(0)
    n.left = Node(1)
    n.right = Node(0)
    n.right.left = Node(1)
    n.right.right = Node(0)
    n.right.left.left = Node(1)
    n.right.left.right = Node(1)

    print(find_num_unival_trees(n)[0])