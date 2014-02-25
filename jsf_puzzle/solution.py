import re, random

control = ' #@;:.?$^&*<'
chunk = r", <<X=\w+>> [%s]+[\w\d]+,>,[\w\d]+[%s]+,>" % ((control,) * 2)
solutionString = "sOluTiOn"[::-1]

valid = re.compile(chunk*8)

def randomControl():
    return random.choice(control)

letterOrNum = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ0123456789'

def randomLetterOrNum():
    return random.choice(letterOrNum)

def randomK():
    return int(random.random() * 20 + 2)

def genJunk(k):
    s = ''
    for u in range(k):
        if random.random() > .5:
            s += randomControl()
        else:
            s += randomLetterOrNum()
    return s

insert = ''
insert += ', <<X='
insert += solutionString + '>> '
insert += ''.join([randomControl() for u in range(randomK())])
insert += ''.join([randomLetterOrNum() for u in range(randomK())])
insert += ',>,'
#insert += ''.join([randomLetterOrNum() for u in range(randomK())])
#insert += ''.join([randomControl() for u in range(randomK())])
insert += ''.join([randomLetterOrNum() for u in range(randomK())])
insert += ''.join([randomControl() for u in range(randomK())])
insert += ',>'

#print chunk
print insert


s = re.search(chunk, insert)
print s.group(0)

def binaryToFormat(binary):
    s = ''
    for i in binary:
        s += '!' if i == '1' else '()'
    return s

hint = 'ConvertFollowingToBase10'

def pad8(i):
    return (bin(i)[2:]).zfill(8)

list6 = '[!()]+'

def encode6(s):
    new = ''
    for c in s:
        ind = list6.index(c)
        new += str(ind + 1)
    return new

def toBinaryFrom10(s):
    big = int(s, 10)
    return bin(big)[2:]

        

starter = ''.join(map(pad8, map(ord, hint)))

f = open('jsfuck.txt','r')
pure = ''
for line in f:
    pure += line.strip()
f.close()
#print pure

encoded = encode6(pure)
print encoded[:100]

binary = toBinaryFrom10(encoded)
print binary[:100]

back = str(int(binary,2))
print back[:100]

binary = starter + binary

encBinary = binaryToFormat(binary)
#print encBinary

final = genJunk(15000) + encBinary + genJunk(22000)

out = open('puzzle.txt','w')
out.write(final)
out.close()
