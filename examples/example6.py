import sys

def match(x: int)->None:
	y = x * 2 - 3
	match y:
		case 5:
			print("hit 5!")
		case 10:
			print("hit 10!")
		case -57 | 42:
			print("really?")
		case _:
			print("you haven't done anything yet")
	return

if __name__ == '__main__':
	x = int(sys.argv[1])
	match(x)