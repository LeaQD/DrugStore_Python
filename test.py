import collections
f = open('Acc.txt', 'r')
chain = collections.ChainMap() 
while True:
    line = f.readline()
    if line == "" :
        break
    if line != "\n":
        s = line.split()
        chain[s[0]] = s[1]
print(chain)
f.close()