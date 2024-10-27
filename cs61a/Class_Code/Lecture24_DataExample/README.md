# Data example
## Class attribute versus instance attribute
* Instance attribute are found before class attribute.
* But when you create an object and you assign the variable that doesn't contain in the __init__ method, it won't find it in class attribute, instead it'll **create it's own instance attribute**
##  List comprehension
* python have some cool tool like **map** , **filter** , and **zip**, to help us select the element we want in very short line.
* map introduce
  * Syntax:map(function, iterator), map will put all the element in the iterator through the function, and the return value is also an iterator
  * ```python
    >>> list1=[1,-2,3]
    >>> x1 = map(abs,list1)
    >>>[x1]
    [1,2,3]
* filter introduce
  * syntax:filter(function,iterator), also bring all the element in the iterator to function, but this function's return value should be True or False, and put the **True value** into the return iterator
  * ```python
    def is_odd(num):
      if num%2==1:
        return True
      return False
    >>> list1 = [1,2,3,4,5]
    >>> ans = filter(is_odd, list1)
    >>> [ans]
    [1,3,5]
 * zip introduce
   * syntax:zip(iteratot1,iterator2),the length of the both iterator must be the same.It will bind the same index element into a tuple, and put all the tuple in the return iterator.
   * ```python
     def largest_adj_sum(s):
      """Largest sum of two adjacent elements in a list s.
      >>> largest_adj_sum([-4, -3, -2, 3, 2, 4])
      6
      >>> largest_adj_sum([-4, 3, -2, -3, 2, -4])
      1
      """
      return max[x+y for x,y in zip(s[:-1],s[1:])]
     
  
