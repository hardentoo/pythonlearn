# https://py.checkio.org/mission/roman-numerals/

n = 3999

i = n // 1000

str = ''

str = str + i * 'M'


n = n % 1000

i = n // 500

str = str + i * 'D'


n = n % 500

i = n // 100

str = str + i * 'C'



n = n % 100

i = n // 50

str = str + i * 'L'



n = n % 50

i = n // 10

str = str + i * 'X'


n = n % 10

m = ['','I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

str = str + m [n]


str = str.replace('CCCC','CD')

str = str.replace('DCD','CM')

str = str.replace('XXXX','XL')

str = str.replace('LXL','XC')


print (str)
