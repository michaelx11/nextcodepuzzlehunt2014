k1 = 'guesses'
s1 = '18.03?$'
k2 = 'differentialequations'
s2 = 'TheRInCLRS, w/middle$'
k3 = 'ronaldlrivest'
#s3 = '18C?->30char$'
s3 = '18C?:30chars$'
k4 = 'mathematicswithcomputerscience'
s4 = 'LookAndSayRealAnalysisWithC  $'
k5 = 'eighteenonehundredc'
s5 = '18CGotNothingON6\d$'
k6 = 'computerscienceandengineering'
s6 = 'YayTheAnswerIsSomeString:yolo'

def xor(s):
    s1 = s[0]
    s2 = s[1]
    return ''.join(map(chr,map(lambda x:ord(x[0])^ord(x[1]), zip(s1,s2))))

def xorK(s1,s2,k):
    return xor((s1[:k],s2[:k]))

def xorBlocks(s1,s2):
    s1 = s1 * 100
    return xorK(s1,s2,len(s2))

sols = [s1, s2, s3, s4, s5, s6]
keys = [k1, k2, k3, k4, k5, k6]

fullstring = ''.join(map(xor,zip(sols,keys)))


print fullstring
print map(ord, fullstring)
f = open('puzzle.txt','w')
f.write(fullstring)
f.close()

f = open('puzzle.txt','r')
string = ''
for line in f:
    string += line.strip()
f.close()

string = string.strip()

print map(ord,string)

for x in keys:
    print 'XOR:',xorBlocks(x, string)
    string = string[len(x):]
    print 'NEW:',string
