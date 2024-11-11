class Tree:
    def __init__(self, label, branches = []):
        for branch in branches:
            assert isinstance(branch, Tree)
        self.label = label
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(repr(self.label), branch_str)
    
    def is_leaf(self):
        return not self.branches

def fib_tree(n):
    if n == 0 or n == 1:
        return Tree(n)
    else:
        right_tree = Tree(n-1)
        left_tree = Tree(n-2)
        fib_n = right_tree.label + left_tree.label
        return Tree(fib_n, [left_tree, right_tree])
def leaves(t):
    if t.is_leaf():
        return [t.label]
    else:
        all_leaves = []
        for branch in t.branches:
            all_leaves.extend(branch)
        return all_leaves
def height(t):
    if t.is_leaf():
        return 0
    else:
        for branch in t.branches:
            return 1 + max(height(branch))

def prune(t, n):
    """Prune all sub-tree whose label is n."""
    t.branches = [b for b in t.branches if b.label != n]
    for b in t.branches:
        prune(b, n)