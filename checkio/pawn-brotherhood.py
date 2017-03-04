# https://py.checkio.org/mission/pawn-brotherhood/

def is_safe (cell, pos):

	strx = "abcdefgh"
	stry = "12345678"

	l = list (cell)
	p = l[0];

	cellx = strx.index(p[0])
	celly = int(p[1]) - 1

	for x in [0,1,2,3,4,5,6,7]:
		
		if ( abs(cellx - x) == 1):

  			for y in [0,1,2,3,4,5,6,7]:
  		
  				if ( celly - y == 1):

  					cell = set([''.join([strx[x],stry[y]])])

  					if (cell < pos):
  						return 1

	return 0


def safe_pawns (pos):

	strx = "abcdefgh"
	stry = "12345678"
	
	count = 0
	
	for x in [0,1,2,3,4,5,6,7]:
	 	for y in [0,1,2,3,4,5,6,7]:
	 		cell = set([''.join([strx[x],stry[y]])])
	 		if ( (cell < pos) & is_safe (cell, pos) ):
	 			count += 1
	 			
	return count 

pos = {"b4", "c4", "d4", "e4", "f4", "g4", "e5"}

print (safe_pawns(pos))
