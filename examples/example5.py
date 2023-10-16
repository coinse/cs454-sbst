def collection(a: int, b: int, c: int)->bool:
	if a in [42, 3817, 1038472]:
		if b > 0 and b < 100:
			if c in set([33, 66, 99]):
				return True
			else:
				return False
		else: 
			return False
	else:
		return False
	return False