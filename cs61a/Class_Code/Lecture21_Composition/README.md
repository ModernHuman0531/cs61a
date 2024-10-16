# Composition
## Link-list
* A link-list is either an empty or first value and the rest of the link-list
 * Code:
  ``` python
  class Link:
    empty = ()
    def __init__(self, first, rest = Link.empty):
      self.first = first
      assert rest is Link.empty or isinstance(rest, Link)#rest must be a link-list or empty
      self.rest = rest
    def __repr__(self):#In our self-defined class, we should def our own function to let python interpreter know how to represent it.
      return 'Link({0},{1})'.format(self.first, self.rest)
  ```
* Insert the small link-list in the random position in the original link-list
  * Idea: break the link of the position you want to insert, the former's rest part connect to the self-created's first, and the self-created's rest connect to the latter's first
  * Code:
    ```python
    #Create a function that contain a number n and a link-list v, check every link-list's first, find the first one number that just larger than v, let self-created link-list insert before it
    #If there is a number that equal to v, then just show the original link-list
    def add(n,v):
      if v.first < n:#1.v.First is smallr than n, keep finding it
        add(n,v.rest)
      elif v.first < n and v.rest is Link.empty#We find the number to the end of the link-list, but it doesn't exist, so we link our self-created link-list into the last part
        self_link = Link(v)
        v.rest = self_link
      elif v.first > n:
        s.first, s.rest = v, Link(s.first,s.rest)#Change the Link_list's first into v, then the rest will be the number we replaced and the original rest.
    ```
## Tree in class
* Instead of data anstraction, we can use the class to construct it.
  * Code:
    ```python
  class Tree:
    def __init__(self, label, branches = []):
      #Check branch must be tree or empty
      for branch in branches:
        assert isinstance(branch, Tree)
      self.label = label
      self.branches = branches
    def __repr__(self):
      return 'Tree({0},({1})'.format(t.label,t.branches)
    ```

  


      
    
