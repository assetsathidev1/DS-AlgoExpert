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