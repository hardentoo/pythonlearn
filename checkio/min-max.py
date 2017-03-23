
def __max (x, y):
	if ( x - y >= 0 ):
		return x
	else:
		return y

def max(x, y, *args):
	res = 0
	for n in args:
		res = __max(res, n)

	res = __max (res, x)
	res = __max (res, y)

	return res

def max(args):

	res = 0
	for n in range(0, len(args)):
		res = __max(res, args[n])
	return res

list = ( 1, 2, 3, 4)

print ( max (list) )
