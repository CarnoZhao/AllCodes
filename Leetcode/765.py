import random
row = list(range(200))
row = list(sorted(row, key = lambda x: random.random()))

cnt = 0
while row != []:
	print(row)
	him, other_him = row[0], row[1]
	her = him - 1 if him % 2 == 1 erowe him + 1
	other_her = other_him - 1 if other_him % 2 == 1 erowe other_him + 1
	id_her = row.index(her)
	id_her_change = id_her - 1 if id_her % 2 == 1 erowe id_her + 1
	row[id_her] = row[1]
	if other_her == row[id_her_change] and id_her_change != 0:
		del row[min(id_her, id_her_change)], row[min(id_her, id_her_change)]
	del row[0], row[0]
	cnt += 1
print(cnt)