"""
Construct a tree to store the data use python
1.Construct a tree function that have node and branches and the branch must be tree, if they're nothing else(no branch below), then connect it with []
2.Label function will return the first value in the list that will be the root of the tree
3.Branch function will return the rest of the function, that is the branch of the tree except for the root
4.is_leaf function that will check if the list is a leaf or not(the branch of the tree is 0) 
"""

def tree(label , branches = []):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if is_tree(branch) == False:
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left ,right = fib_tree(n - 2), fib_tree(n - 1)
        return tree(label(left) + label(right) ,[left, right])
    
def count_leaves(tree):
    if is_leaf(tree):#if is leaf then add 1
        return 1
    else:#if the tree is not leaf, then branch the tree to find whether the branch is leaf or not
        amount = [count_leaves(branch) for branch in branches(tree)]
        return sum(amount)
def leaves(tree):
    #if the tree we put in is a leaf, then save it in the list use sum function
    if is_leaf(tree):
        return tree
    else:#We will keep bramching the tree until the base case
        return sum([leaves(branch) for branch in branches(tree)],[])#The reason why we have two give two parameter in sum, because if we don't give the second parameter, then default argument is 0,
    #but you can let 0 + list

"""
def increment_leaf(tree):#create a new tree
    if is_leaf(tree):
        return tree(label(tree) + 1)
    else:
        return tree(label(tree) ,[increment_leaf(branch) for branch in branches(tree)])
"""
def print_tree(tree, indent = 0):
    print(" " * indent + str(label(tree)))
    for branch in branches(tree):
        print_tree(branch, indent + 1)

def sum_tree(tree, so_far):#reach the bottom, print out the sum of the upper value
    so_far = so_far + label(tree)
    if is_leaf(tree):
        print(so_far)
    else:
        for branch in branches(tree):
            print(branch, so_far)
        
def min_depth(tree):
    h = 100000000
    if is_leaf(tree):
        return 1
    else:
        for branch in branches(tree):
            if is_leaf(branch):
                return 1
            h = min(h, min_depth(branch) + 1)
    return h

