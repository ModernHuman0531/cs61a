# Homework problem
## Problem 3. Store digits
* Write a function store_digits that takes in an integer n and returns a linked list where each element of the list is a digit of n.
* Key_idea: Link1 = Link(1), if we want to create a new link that the rest is Link1, we can write: Link1 = Link(2,Link1), so that Link1 = Link(2,Link(1))
  ```python
  """
  >>> store_digits(345)
  Link(3,Link(4,Link(5)))
  """
  def store_digits(num):
    ans = Link.empty
    while num:
      ans = Link(num % 10, ans)
      num = num//10
    return ans
  ```
## Problem 4.Is bst
* The definition of Binary Search Tree(bst)
    * The bst has at most two childern
    * The childern must also be the bst, leaf is counted as bst
    * The left child's label must be smaller or equal to the node's label
    * The right child's label must be larger than the node's label
* We are asked to write the code that judge whether the tree is bst or not by using the chracteristic above
    * Code:
      ```python
      def is_bst(t):
        """We can implement two helper function: bfs_max and bfs_min to help us, two function have a demanded condition, is that we trust the tree is bst
        bst_min(t) is a function that return smallest label of the bfs
        bst_max(t) is a function that return largest label of the bfs
        And then we discuss the bst in three condition:1.One branch 2. Two branches 3.Other
        """
        def bst_min(t):
          if t.is_leaf():
            return t.label
          else:#Compare with the most left branches
            return min(t.label,bfs_min(branches[0])
        def bst_max(t):
          if t.is_leaf():
            return t.label
          else:
            return max(t.label,bst_max(branches[-1]))
        if t.is_leaf():
          return True
        if len(branches) == 1:
          c = branches[0]
          return is_bst(c) and (t.label >= bst_min(c) or t.label < bst_max(c))
        elif len(branches) == 2:
          c1, c2 = branches[0], branches[1]
          return is_bst(c1) and is_bst(c2) and t.label >= bst_max(c1) and t.label < bst_min(c2)
        else:
          return false
      ```
          
        

         
  
