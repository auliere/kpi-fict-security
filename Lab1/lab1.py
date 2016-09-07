import string
import pprint
from operator import itemgetter

freq = {}
sample = [('E', 12.02), ('T', 9.10), ('A', 8.12), ('O', 7.68), ('I', 7.31), ('N', 6.95), ('S', 6.28), ('R', 6.02), ('H', 5.92), ('D', 4.32), ('L', 3.98), ('U', 2.88), ('C', 2.71), ('M', 2.61), ('F', 2.30), ('Y', 2.11), ('W', 2.09), ('G', 2.03), ('P', 1.82), ('B', 1.49), ('V', 1.11), ('K', 0.69), ('X', 0.17), ('Q', 0.11), ('J', 0.10), ('Z', 0.07)]
s = open('ctext.txt').read()
su = s.upper()
a = string.uppercase
l = len(su)
print l
print su.count('A')
print (su.count('A')+0.0)/l
for c in a:
    freq[c] = round((su.count(c) + 0.0)/l * 100,3)
freq = sorted(freq.items(), key=itemgetter(1), reverse = True)
blah = sorted(zip(sample, freq), key = lambda x: x[0][0])
pprint.pprint(blah)
x = {}
for a in blah:
    x[a[1][0]] = a[0][0]
res = ''

for c in su:
    if c in x.keys():
        c = x[c]
    res += c
pprint.pprint(res)