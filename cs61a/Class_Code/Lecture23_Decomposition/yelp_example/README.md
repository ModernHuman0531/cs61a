# Decomposition
## Fast_overlap:
* A simple alogrithm that help us find the smae element of two sorted list(list1 and list2).
  * If $list1's[0] > list2's[0]$, list2's index += 1
  * If $list1's[0] < list2's[0]$, list1's index += 1
  * If $list1's[0] == list2's[0]$, both index += 1
  * Code:
    ```python
    def fast_overlap(list1, list2):
      i, j = 0, 0
      count = 0
      while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
          j += 1
        elif list1[i] < list2[j]:
          i += 1
        else:
          i, j, count = i + 1, j + 1, count + 1
      return count
    ```
## Set
* Set is also a build-in container
  * Set will automatically sort it, but doesn't also sort as you expected.
  * Set will remove the same element in it.
  * Have a constant time to find the element is whether in the set or not.
  * We can also use the set to acheive the fast_overlap easily
  * Code:
  ```python
  def faster_overlap(list1, list2)"
    set1, set2 = set(list1), set(list2)
    intersect_set = list1.intersection(list2)
    return len(intersect_set)
  ```
## Enumerate
* Use recurssion to yield all the possibility combination of the number
* Code:
  ```python
  """
  >>> build(123)
  [1,12,13,123,2,23,3]
  """
  def build(seed):
  if seed == 0:
    yield 0
  else:
    for x in build(seed//10):
      #Take 123 as an example, chooose to add 3 or not.
      yield x
      yield x * 10 + seed % 10
