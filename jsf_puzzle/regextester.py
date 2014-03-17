import re

f = open('puzzle.txt','r')
s = ''
for line in f:
    s += line.strip()
f.close()

pat = re.compile('>>X=.{1,9}<<')
print pat.findall(s)
