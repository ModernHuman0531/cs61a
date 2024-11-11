# Q6: Reverse Other
* Write a function reverse_other that mutates the tree such that labels on every other (odd-depth) level are reversed.
  For example, Tree(1,[Tree(2, [Tree(4)]), Tree(3)]) becomes Tree(1,[Tree(3, [Tree(4)]), Tree(2)]). Notice that the nodes themselves are not reversed;
  only the labels are.
* Code:
  ```python
  def reverse_other(t):
    """Mutates the tree such that nodes on every other (odd-depth) level
    have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    "*** YOUR CODE HERE ***"
    """Just do the stuff for the odd ignore the even"""
    if t.is_leaf():
      return
    else:
      #Find all the label of the branches
      new_label = [b.label for b in t.branches]<2,6,8>
      #Reverse the label
      for i in range(len(t.branches)):<8,6,2>
        t.branches.label[i] = new_label[-i-1]
        #ignore the branch do the branch.branch
        for grandson in t.branches.branches:
          reverse_other(grandson)
    ````
  
      
