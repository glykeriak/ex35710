f=open('two_cities_ascii.txt','r')
lines=f.read()
f.close()
#convert words to binary form of length 7
import math
def toBinary (a):
    k,n=[],[]
    for i in a :
        k.append(ord(i))
    for i in k:
        n.append(int(bin(i)[2:]))
    return n
binary=toBinary(lines)
binarystr = [str(x) for x in binary]
for i in range(0,len(binarystr)):
    if len(binarystr[i])<7:
        mis=7-len(binarystr[i])
        binarystr[i]="0"*mis+binarystr[i]
#keeps 4 of the bits and separates them in groups of 16
for i in range(0,len(binarystr)):
    keep=binarystr[i][0:2]
    keep2=binarystr[i][5:7]
    totalkeep=keep+keep2
    binarystr[i]=totalkeep
str="".join(binarystr)
import textwrap
wrapper=textwrap.TextWrapper(width=16)
list=wrapper.wrap(text=str)
for i in range(0,len(list)):
    list[i]=int(list[i])
pl0=0
pl1=0
pl2=0
pl3=0
#prints the statistics
for i in range(0,len(list)):
    if list[i]%2==0:pl0+=1
    if list[i]%3==0:pl1+=1
    if list[i]%5==0:pl2+=1
    if list[i]%7==0:pl3+=1
print((pl0/len(list))*100," % divided by 2")
print((pl1/len(list))*100," % divided by 3")
print((pl2/len(list))*100," % divided by 5")
print((pl3/len(list))*100," % divided by 7")
