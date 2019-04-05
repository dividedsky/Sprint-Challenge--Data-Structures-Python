Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
* I think it's O(1). Inserting into the middle of the list would be O(n) because everything in the list would have to move, but we're not doing that. We're just replacing items in the list with new items.

2. What is the space complexity of your ring buffer's `append` function?
* O(n), where _n_ is the capacity of the list.

3. What is the runtime complexity of your ring buffer's `get` method?
* O(n). Since we need to rebuild the list to strip out None values, the complexity will depend on the capacity of the list.

4. What is the space complexity of your ring buffer's `get` method?
* O(n)


5. What is the runtime complexity of the provided code in `names.py`?
* O(n^2), since we have nested for loops looping through the names

6. What is the space complexity of the provided code in `names.py`?
* I think it's O(n), since we're building lists based on the number of names

7. What is the runtime complexity of your optimized code in `names.py`?
* O(n logN), since we're using a binary search tree to insert and retrieve names, but still have to traverse one whole list to build the search tree.

8. What is the space complexity of your optimized code in `names.py`?
* Still O(n), I think.
