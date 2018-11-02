f = open('kaartnummers.txt', 'r')
max = -1
lineNum = -1
line = f.readline()
index = 0
while(line):
    index+=1
    newNum = int(line[:6])
    if(newNum>max):
        max = newNum
        lineNum = index
    line = f.readline()
print("Deze file telt {} regels \n Het grootste kaartnummer is {} en dat staat op regel {}" .format(index, max, lineNum))
f.close()