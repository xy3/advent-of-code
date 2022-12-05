import sys

wins = {'A': 'B','B': 'C','C': 'A'}
loses = {'A': 'C','B': 'A','C': 'B'}

scores = {'A': 1,'B': 2,'C': 3}
score = 0

for l in sys.stdin:
    first, second = l.strip().split()
    token = ""
    if second == "X":
        token = loses[first]
    elif second == "Y":
        token = first
        score += 3
    else:
        token = wins[first]
        score += 6

    score += scores[token]

print(score)