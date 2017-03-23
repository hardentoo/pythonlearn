# https://py.checkio.org/mission/non-unique-elements/

m = [1,1,1,2,2,2,3,3,3,1,1,1,2,2,2,3,3,3,5,1,7,1,9,2,3]

i = 0

r = []

while i != len(m):
    if (m.count(m[i]) > 1):
    	r.append(m[i])
    i = i + 1

print (r)