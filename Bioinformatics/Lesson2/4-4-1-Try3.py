masstable = [97, 99, 113, 114, 128, 147, 163, 186]
prolist = [[]]
def recursion(prolist, n, masstable, mass):
	for protein in prolist:
		for aa in masstable:
			protein += [aa]
			promass = sum(protein)
			if n != 1:
				prolist += [protein] if promass < mass else []
			elif n == 1 and promass == mass:
				prolist.append(protein)
	return prolist