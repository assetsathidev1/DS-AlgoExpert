"""
input:[
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"]
]
results: [0, 0, 1]
output: "Python" 
"""

# o(n) in time | o(n) in space
def tournamentWinner(competitions, results):
    # Write your code here.
    d = {}
    winner_team = None
    winner_score = 0
    for i in range(len(competitions)):
        tup = competitions[i]
        res = results[i]
        if res:
            ws = tup[0]
        else:
            ws = tup[1]
        if ws in d:
            d[ws] += 30
        else:
            d[ws] = 30
        if d[ws] > winner_score:
            winner_team = ws
            winner_score = d[ws]
    return winner_team
