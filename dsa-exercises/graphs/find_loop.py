"""
given a graph in adjacency list format, check if it has a cycle or loop.
input edges:
[
  [1, 3],
  [2, 3, 4],
  [0],
  [],
  [2, 5],
  [2, 5],
  []
]

output: true
"""

# def check_loop_with_bfs(start_index, edges):
#     bfs_idxs = edges[start_index]
#     # print("start bfs_idxs:", bfs_idxs)
#     while bfs_idxs:
#         if start_index in bfs_idxs:
#             return True
#         idx = bfs_idxs.pop(0)
#         bfs_idxs.extend(edges[idx])
#         # print("bfs_idxs:", bfs_idxs)
#     return False

# O(v+e) time | O(v) in space
def check_loop_with_dfs(visited_idxs, curr_idx, edges):
    visited_idxs.add(curr_idx)
    for vidx in visited_idxs:
        if vidx in edges[curr_idx]:
            return True
    for child_idx in edges[curr_idx]:
        return check_loop_with_dfs(visited_idxs, child_idx, edges)
    return False

def cycleInGraph(edges):
    # index array contains itself then return true
    # one soln: apply dfs from each index and see if finds itself
    start_idx = 0
    len_verts = len(edges)
    while start_idx < len_verts:
        if start_idx in edges[start_idx]:
            return True
        r = check_loop_with_dfs(set([]), start_idx, edges)
        if r:
            return True
        start_idx += 1
    return False
