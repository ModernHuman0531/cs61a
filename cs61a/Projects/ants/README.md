# Important concept
* Class attribution
  * When encounter the parameter you want to differ from parent's class with child's class (**Inheritance relationship**), we should put that parameter in the **Class Attribution** instead of instance attribution.
* List Iteration caution:
  * When you iterate over the list, and changing the element in it at the same time, you may not visit all the element.
    ```python
    lst = [1,1,2,2,3,3]
    for elem in lst:
      if elem % 2 == 0:
        lst.remove(elem)
    >>> lst = [1,1,2,3,3]
    ```
  * To deal this problem, we can create a copy of the list, and iterate over it, then change the original list.
    ```python
    lst = [1,1,2,2,3,3]
    copy_lst = lst[:]#<- Make the copy of the list, don't just give the equal symbol
    for elem in copy_lst:
      if elem % 2 == 0:
        lst.remove(elem)
    >>> lst = [1,1,3,3]
    
     
