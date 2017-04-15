# Генерируем большую строку из данной по функции

def f(n):
        return n**3+1

str = "abcdefghigklmnoprstuwxyz"

a = 0

print (len(str))

strall = ''

while a < 100:
        a = a + 1
        strall = strall +  str [ ( f(a) % len(str) ) : ( f(2*a) % len(str) )]

print (strall)

