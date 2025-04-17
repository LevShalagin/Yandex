DB = []
res = {}

for _ in range(int(input())):
    DB.append(input().split())

# приводим к удобной для вычеслений форме
for i in range(len(DB)):
    DB[i] = [int(DB[i][0]) * 24 * 60  + int(DB[i][1]) * 60 + int(DB[i][2])] + [int(DB[i][3])] + [DB[i][4]]

# сортируем по времени и идентификатору
DB.sort(key=lambda x: x[0])
DB.sort(key=lambda x: x[1])


for id, record in enumerate(DB):
    if record[1] not in res.keys():
        res[record[1]] = 0
        continue
    if record[-1] in ['B', 'S', 'C']:
        res[record[1]] += (record[0] - DB[id - 1][0])

print(*res.values())
