"""
input array: [1, 1, 3, 2, 1]
output: 4
trick is: peak is defined as a number that is strictly greater than its adjacent numbers
and the peak is not the first or last number in the array
see if current number is a peak, if not, move on
if it is a peak, then find the length of the peak by going left and right
"""

# o(n) in time | o(1) in space
def longestPeak(array):
    i = 1
    max_peak_len = 0
    while i < len(array)-1:
        is_peak = array[i] > array[i-1] and array[i] > array[i+1]
        # print(i, is_peak)
        if not is_peak:
            i += 1
            continue
    
        left_idx = i - 2
        while left_idx >= 0 and array[left_idx] < array[left_idx+1]:
            left_idx -= 1
        right_idx = i + 2
        while right_idx < len(array) and array[right_idx] < array[right_idx-1]:
            right_idx += 1

        # print(i, "ri:", right_idx, "li:", left_idx)
        current_peak_len = right_idx - left_idx - 1
        max_peak_len = current_peak_len if max_peak_len < current_peak_len else max_peak_len
        # print(i, "c:", current_peak_len, "m:", max_peak_len)
        i = right_idx
    return max_peak_len
