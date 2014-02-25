import re

expr = '[!()]+'

first = re.compile(expr)

f = open('puzzle.txt','r')
s = ''
for line in f:
    s += line.strip()
f.close()

#print s

match = first.search(s).group()

print match

def convertToBinary(s):
    index = 0
    news = ''
    while index < len(s):
        if s[index]=='!':
            news += '1'
            index += 1
        else:
            news += '0'
            index += 2
    return news

binary = convertToBinary(match)

print binary

def parseK(s,k):
    news = ''
    for i in range(0, k * 8, 8):
        news += chr(int(s[i:i+8],2))
    return news

firstChunk = parseK(binary,100)
print 'yo',firstChunk

le = len('ConvertFollowingToBase10') * 8

remaining = binary[le:]

base10 = str(int(remaining,2))
print base10

def mapBack(s):
    news = ''
    for i in s:
        news += expr[int(i) - 1]
    return news

f = open('output.txt','w')
f.write(mapBack(base10))
f.close()
