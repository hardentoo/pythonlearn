# https://py.checkio.org/mission/cipher-map2/

key = ('X...', '..X.', 'X..X', '....')

password = ('itdf', 'gdce', 'aton', 'qrdi')

def rotate(key):
	
	_key = [ [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0] ]

	for i in [0,1,2,3]:
		for j in [0,1,2,3]:
			_key[j][3-i] = key[i][j]
	return _key

print(rotate(key))

def recall_password (key, password):

	res = []

	for k in [0,1,2,3]:

		for i in [0,1,2,3]:
			for j in [0,1,2,3]:
				if (key[i][j] == 'X'):
						res += password[i][j]
		key = rotate(key)	

	str = ''

	return str.join(res)


print (recall_password (key,password))