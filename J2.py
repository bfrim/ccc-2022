n = int(input())

good_scores = 0

for i in range(n):
    points = int(input())
    fouls = int(input())

    individual_score = (points * 5) - (fouls * 3)

    if individual_score > 40:
        good_scores += 1

if good_scores == n:
    print("{}+".format(good_scores))
else:
    print(good_scores)
