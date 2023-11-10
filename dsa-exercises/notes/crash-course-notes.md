# DSA Crash course notes

## Complexity Analysis
- Time complexity is the amount of time taken by an algorithm to run; as a function of the length of the input.
- Space complexity is the amount of memory taken by an algorithm to run; as a function of the length of the input.  
- Comparing 2 solutions can be done by comparing their time and space complexities and choosing the one with the least complexity.
- Its important to know the time and space complexities of the most common data structures so as to choose the right one for the problem at hand.

### Memory
- 1 Byte is 8 bits. Any number can be represented in binary form using binary bits.
- Most modern computers have 64 bit architecture, which means that they can process 64 bits of data at a time.
    - `int` is a 32 bit data type, which means that it can store 32 bits of data at a time OR 4 Bytes of data at a time. 
    - This means that the max number that can be stored in an `int` is $2^{32} - 1$.
    - Similarly `long` is a 64 bit data type, which means that it can store 64 bits of data at a time or 8 Bytes of data at a time.
    - This means that the max number that can be stored in a `long` is $2^{64} - 1$.
- `Endianess` is the order in which the bytes are stored in memory. There are 2 types of endianness: `Big Endian` and `Little Endian`. 
- `Big Endian` means that the **most significant byte is stored first** and the **least significant byte is stored last**.
- `Little Endian` means that the **least significant byte is stored first** and the **most significant byte is stored last**.
    - Decimal numbers are also stored in binary form, but they are stored in a different format called `IEEE 754` format.
    - `float` is a 32 bit data type, which means that it can store 32 bits of data at a time or 4 Bytes of data at a time.
    - `double` is a 64 bit data type, which means that it can store 64 bits of data at a time or 8 Bytes of data at a time.
    - An example of a `float` number is `3.14`, which is stored in binary form as `11.0010001011011110` 
    here the first bit is the sign bit, the next 8 bits are the exponent bits and the remaining 23 bits are the mantissa bits. 
    - The mantissa represents the actual digits of the number.
    - The exponent determines where the decimal (or binary) point should be placed relative to the beginning of the mantissa.
- An array of numbers are saved in memory in a contiguous manner. Say there is an array of 2 integers, then the first integer will be stored in the first 4 bytes and the second integer will be stored in the next 4 bytes.
- Each memory slot (say 1 byte) can store 1 byte of information. This byte could represnet an actual number or a character or a boolean value OR **a pointer** to another memory location.
- Each memory slot has an address associated with it. This address is called the `pointer` to that memory location. The address itself is a binary number.
- Accessing any memory location is done in constant time, considered a very cheap operation.

### Big O Notation
- This notation is used to describe the time and space complexities of an algorithm.
- Common complexities are as follows (listed in the order of increasing complexity):
    - $O(1)$ - Constant time/Space  (ex: accessing an array element)
    - $O(log(n))$ - Logarithmic time/Space  (ex: binary search)
    - $O(n)$ - Linear time/Space  (ex: linear search)
    - $O(nlog(n))$ - Log Linear OR Linearithmic time/Space  (ex: merge sort)
    - $O(n^2)$ - Quadratic time/Space (ex: pairwise comparison)
    - $O(n^3)$ - Cubic time/Space  (ex: 3 nested loops)
    - $O(2^n)$ - Exponential time/Space  (ex: recursive fibonacci)
    - $O(n!)$ - Factorial time/Space  (ex: travelling salesman problem)
- Big O notation is used to describe the **worst case** time and space complexities of an algorithm.
- $O(log(n))$ Logarithmic complexity intuation: Am i halfing the number of elements i need to check at every step; OR as my input size doubles am i only increasing the number of steps by 1.

## Data Structures

### Arrays
- Arrays are a collection of elements of the same data type with contiguous memory allocation. Starting with index 0
- The complexity for standard operations are as follows:
    - Accessing an element at a given index: $O(1)$
    - Updating an element at a given index: $O(1)$
    - Inserting an element at a given index: $O(N)$
    - Deleting an element at a given index: $O(N)$
    - Searching for an element: $O(N)$
    - Copying an array: $O(N)$
- Arrays can be Static or Dynamic. Static arrays have a fixed size, while dynamic arrays can grow in size.
- Dynamic arrays are implemented using static arrays. When the dynamic array is full, a new static array is created with double the size of the previous array and all the elements are copied to the new array.
- The complexity for standard operations for dynamic arrays are as follows:
    - Accessing an element at a given index: $O(1)$
    - Updating an element at a given index: $O(1)$
    - Inserting an element at the end of the array: $O(1)$
    - Inserting an element at a given index: $O(N)$
    - Deleting an element at a given index: $O(N)$
    - Searching for an element: $O(N)$
    - Copying an array: $O(N)$

### Linked Lists
- Linked Lists are a collection of elements of the same data type with non-contiguous memory allocation.
- LLs are implemented using nodes. Each node has a value and a pointer to the next node.
- The obvious issue with array, is the requirement of contiguous memory allocation. This is solved by LLs.
- Typcally we have a head node and a tail node. The head node is the first node in the LL and the tail node is the last node in the LL.
- The complexity for standard operations are as follows:
    - Accessing an element at Head node: $O(1)$
    - Accessing an element at Tail node: $O(N)$
    - Accessing an element at a given index: $O(N)$
    - Insert / Remove element at Head: $O(1)$
    - Insert / Remove element at Tail: $O(N)$
    - Searching for an element: $O(N)$
- Doubly Linked Lists are a type of LLs where each node has a pointer to the previous node as well as the next node.
- The complexity for standard operations for DLLs are as follows:
    - Accessing an element at Head node: $O(1)$
    - Accessing an element at Tail node: $O(1)$
    - Accessing an element at a given index: $O(N)$
    - Insert / Remove element at Head: $O(1)$
    - Insert / Remove element at Tail: $O(1)$
    - Searching for an element: $O(N)$
- Circular Linked Lists are a type of LLs where the tail node points to the head node.

### Hash Tables
- Hash Tables are a collection of elements with non-contiguous memory allocation.
- Hash Tables are implemented using an array of buckets. Each bucket is a linked list.
- Hash Tables are used to store key-value pairs.
- The key is hashed to get an index. The value is stored in the bucket at that index.
- The complexity for standard operations are as follows:
    - Inserting an element: $O(1)$ , worst case $O(N)$
    - Updating an element: $O(1)$ , worst case $O(N)$
    - Deleting an element: $O(1)$ , worst case $O(N)$
    - Searching for an element: $O(1)$ , worst case $O(N)$
    - Storing all the elements: $O(N)$ in time and space complexity
- Collisions occur when 2 keys are hashed to the same index. This is solved by using a linked list at each bucket.
- Hashing functions are gotten very good at distributing the keys evenly across the buckets.
- Resizing the number of buckets is done when the load factor (ratio of number of elements to number of buckets) is greater than a certain threshold.

### Stacks and Queues
- Stacks and Queues are abstract data types. They are not built into the language.
- Stacks are a list of elements that follow Last In First Out (LIFO) order
- Queues are a list of elements that follow First In First Out (FIFO) order
- Stacks can be implemented using dynamic arrays or linked lists.
- Queues can be implemented using doubly linked lists.
- Constant Space Time for push/pop and enqueue/dequeue operations.
- Search for element in both takes $O(N)$ time complexity and $O(1)$ space complexity.
- Peek operation takes $O(1)$ time complexity and $O(1)$ space complexity.

### Strings
- Strings are immutable in Java, Python, JS etc. This means that once a string is created, it cannot be changed.
- So any additions or deletions to a string will create a new string. Hence is a more expensive operation than usual array operations.
- Strings are saved in memory as an array of characters.
- `ASCII` is a character encoding standard that uses 7 bits to represent each character. This means that there are 128 characters that can be represented using `ASCII`.
- `Unicode` is a character encoding standard that uses 16 bits to represent each character. This means that there are 65536 characters that can be represented using `Unicode`.
- Traverse is going to be $O(N)$ time complexity, where N is the length of the string.
- Copy string is going to be $O(N)$ space time complexity, where N is the length of the string.
- Concatenation of 2 strings is going to be $O(N+M)$ time complexity
- `C++` strings are mutable, so they can be changed in place.
- `KMP (Knuth-Morris-Pratt) algo` is used to find a substring in a string in linear time.

### Graphs
- A graph is a collection of nodes and edges. Nodes are also called vertices. Edges are also called links.
- Graphs can be directed or undirected. In a directed graph, the edges have a direction associated with them. In an undirected graph, the edges do not have a direction associated with them.
- Graphs can have cycles or no cycles. A cycle is a path that starts and ends at the same node.
- Its important to note vertices previously visited in order to not get stuck in infite loops, while traversing cyclical graphs
- Saved in memory as an adjacency list or an adjacency matrix.
- Space complexity for storing a graph is $O(V+E)$
- Traversal of a graph is done using Breadth First Search or Depth First Search.
- Time complexity of traversal is $O(V+E)$

### Trees
- Tree is a type of a graph. A tree is a connected graph with no cycles, a fixed root node and a heirarchical/directed structure. No cycles means that there is only one path from the root node to any other node in the tree.
- K-ary tree is a tree where each node has at most K children. Binary tree is a tree where each node has at most 2 children.
- There are trees that satisy spl conditions which are used in various ways. Example: BST, Trie etc.
- A tree is full if every node has either 0 or K children. A tree is complete if every level except the last level is full and the last level is filled from left to right.
- A complete binary tree is a binary tree where every level except the last level is full and the last level is filled from left to right.
- A heap is a complete binary tree that also satisfies the heap property. A heap is a tree where the value of the parent node is greater than or equal to the value of the child nodes.
- Min Heap is a heap where the value of the parent node is less than or equal to the value of the child nodes. 
- Max Heap is a heap where the value of the parent node is greater than or equal to the value of the child nodes.
