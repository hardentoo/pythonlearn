
def decrypt (str):

	key = "abcdefghijklmnopqrstuvwxyz"

	result = ""

	for i in range(0,len(str)):
		c = str[i]
		if ( c.isalpha() == False ):
			result += c
			continue
		result += key[(key.find(c) + 2) % len(key)]
	
	return result

str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print(decrypt(str))

print(decrypt("map"))