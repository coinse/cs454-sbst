def foo(x: int, y: int) -> int:
	z = 0
	if x == 42:
		if y == 0:
			z = 1
		else:
			z = 0
	else:
		z = -1
	return z

def bar(x: int, y: int, z: int) -> int:
	if (x + y) / 2 > z:
		return z
	elif (x + y) / 3 < z and x > y:
		return x
	else:
		return y
