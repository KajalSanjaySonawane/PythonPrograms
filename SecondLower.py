ls = []
second_lowest_names = []
scores = set()

for _ in range(int(input())):
    name = input()
    score = float(input())
    ls.append([name, score])
    scores.add(score)

print(ls)

second_lowest = sorted(scores)[1]

for name, score in ls:
    if score == second_lowest:
        second_lowest_names.append(name)

print(second_lowest_names)
for name in sorted(second_lowest_names):
    print(name, end='\n')