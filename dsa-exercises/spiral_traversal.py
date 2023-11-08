"""
input: [
  [1, 2, 3, 4],
  [12, 13, 14, 5],
  [11, 16, 15, 6],
  [10, 9, 8, 7]
]
output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16]
"""


# o(n) in time | o(n) in space -> can clean up a lil bit
def print_perimeter(array, row_len, col_len):
    out_arr = []
    row_offset = 0
    col_offset = 0
    max_ele = row_len * col_len
    while len(out_arr) < max_ele:
        i = row_offset
        j = col_offset
        # print(row_len, col_len, out_arr)
        while j < col_len - col_offset:
            out_arr.append(array[i][j]) 
            j += 1
        j -= 1
        i += 1
        if len(out_arr) >= max_ele:
            break
        # print(i, j, out_arr)
        while i < row_len - row_offset:
            out_arr.append(array[i][j])
            i += 1
        i -= 1
        j -= 1
        if len(out_arr) >= max_ele:
            break

        # print(i, j, out_arr)
        while j >= col_offset:
            out_arr.append(array[i][j])
            j -= 1
        j += 1
        i -= 1
        if len(out_arr) >= max_ele:
            break

        # print(i, j, out_arr)
        while i > row_offset:
            out_arr.append(array[i][j])
            i -= 1
        if len(out_arr) >= max_ele:
            break
        # print(i, j, out_arr)
        row_offset += 1
        col_offset += 1
    return out_arr

def spiralTraverse(array):
    # Write your code here.
    out_arr = print_perimeter(array, len(array), len(array[0]))
    
    return out_arr
