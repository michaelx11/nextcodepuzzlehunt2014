import math, time, datetime, operator

a,b,c,d,e = list('magic')
st = reduce(operator.concat, [a,b,c,d,e])
def magic(magic):
    return magic + datetime.timedelta(seconds=13265)

def magicmagic(magic):
    return magic + datetime.timedelta(seconds=3780)

def magicmagicmagic(magic):
    return magic + datetime.timedelta(seconds=1234517380)

def magicmagicmagicmagic(magic):
    return magic + datetime.timedelta(seconds=2051308800)

def magicmagicmagicmagicmagic(magic):
    return magic + datetime.timedelta(seconds=1924356802)

a,b,c,d = list(range(2))

print magic(magicmagic(magicmagicmagic(magicmagicmagicmagic(magicmagicmagicmagicmagic(datetime.datetime.fromtimestamp(213119878861))))))
