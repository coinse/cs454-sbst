def testme(a: int, b: int, c: int) -> None:
	while a < b:
		if c > 57 and c < 284:
			a += 1
		else:
			a -= 1

		if a < 0:
			break
	return