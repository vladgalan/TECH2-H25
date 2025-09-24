"""
Part 2, Lecture 1

Implement and test argmax() function that returns the location of a maximum.

Tasks
-----

1.  Implement a function argmax() that takes a sequence of numbers and returns 
    the index (position) the maximum element.

2.  Test the function with the following sequence of numbers:
    [2, 3, -1, 7, 4]

3.  Add error handling if an empty sequence is passed. Test the function with an 
    empty sequence.

4.  Use the notebook lecture1-benchmark.ipynb to benchmark your implementation 
    against NumPy's argmax().
"""

import numpy as np

def argmax(Listin:list) -> int:
    if len(Listin) == 0:
        print("List is empty error")
        return None
    else:
        index_dict = {Listin[i]:i for i in range(0, len(Listin))} 
        max_index = index_dict[np.array(Listin).max()]
        print(index_dict)
        return max_index
        
        """numpy solution
        Arr = np.array(Listin)
        max_index = np.where(Listin = Listin.max())[0]
        print(max_index)

        show off solution
        arr.index(max(arr))
        """

print(argmax([1, 10, -1, 7, 4]))
print(argmax([]))

