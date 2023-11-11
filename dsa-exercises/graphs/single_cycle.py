"""
Given an array [1, 1, 1, 1, 2], where each value represents the number of steps to jump forward in the array, determine if the array has a single cycle. 
A single cycle occurs if starting at any index in the array and following the jumps, every element in the array is visited exactly once before landing back on the starting index.

intuation i followed: at the end of len_array jumps, the next_idx should be 0 and the visited_idx should be equal to len_array
tt: 35mins
"""


# O(N) in space and time
def hasSingleCycle(array):
    len_array = len(array)
    visited_idx = set([])
    jump_count = 0
    next_idx = 0
    while jump_count < len_array:
        visited_idx.add(next_idx)
        next_idx = next_idx + array[next_idx]
        next_idx = next_idx % len_array
        if next_idx < 0:
            next_idx = len_array + next_idx
        # print("next i:", next_idx)
        jump_count += 1
        
    # print("visited_idx:", visited_idx)
    if next_idx == 0 and len(visited_idx) == len_array:
        return True
    return False
    
    
