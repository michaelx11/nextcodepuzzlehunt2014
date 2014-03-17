import re, random

control = ' #@;:.?$^&*<>=-_+'
chunk = ">>X=?<<"
regex = ">>X=\w+<<"
solutionString = "gRu.MpY!"

def randomControl():
    return random.choice(control)

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'

def randomLetter():
    return random.choice(letters)

def randomNum():
    return random.choice(nums)

def randomK():
    return int(random.random() * 20 + 2)

def genJunk(k):
    s = ''
    for u in range(k):
        p = random.random()
        if p < .3:
            s += randomControl()
        elif p < .9:
            s += randomLetter()
        else:
            s += randomNum()
    return s

insert = '>>X=%s<<' % solutionString
#insert += ', <<X='
#insert += solutionString + '>> '
#nsert += ''.join([randomControl() for u in range(randomK())])
#insert += ''.join([randomLetterOrNum() for u in range(randomK())])
#insert += ',>,'
#insert += ''.join([randomLetterOrNum() for u in range(randomK())])
#insert += ''.join([randomControl() for u in range(randomK())])
#insert += ''.join([randomLetterOrNum() for u in range(randomK())])
#insert += ''.join([randomControl() for u in range(randomK())])
#insert += ',>'

#print chunk
print insert


#s = re.search(regex, insert)
#print s.group(0)

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

final = genJunk(79120) + encBinary + genJunk(38000) + insert + genJunk(69123) 

out = open('puzzle.txt','w')
out.write(final)
out.close()
