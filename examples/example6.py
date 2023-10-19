def match(x: int)->None:
	y = x * 2 - 3
	match y:
		case 5:
			print("hit 5!")
		case 11:
			print("hit 10!")
		case -57 | 43:
			print("really?")
		case _:
			print("you haven't done anything yet")
	return