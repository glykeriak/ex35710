f= open('two_cities_ascii.txt','r')
lines= f.read()
f.close()
list =('abcdefghijklmnopqrstuvwxyz \nABCDEFGHIJKLMNOPQRSTUVWXYZ')
answer = ''.join(filter(list.__contains__,lines))
words=[]
words.append(answer)
words= answer.split()
sumlist=[]
sumlist=[len(i)for i in words]
sumlist.sort()
max=20
for i in range(0,19):
    if sumlist.count(i)>sumlist.count(max):
        for j in range (0,sumlist.count(max)):
            sumlist.remove(max)
            sumlist.remove(20-max)
    if sumlist.count(i)<sumlist.count(max):
        for j in range (0,sumlist.count (i)):
            sumlist.remove(i)
            sumlist.remove(20-i)
    if sumlist.count(i)==sumlist.count(max):
        if sumlist.count(i) %2==0:
            for j in range (0,sumlist.count(i)):
                sumlist.remove(i)
        elif sumlist.count(i) % 2==1:
            for j in range (0,sumlist.count(i)-1):
                sumlist.remove(i)
    max=max-1
min=sumlist[0]
max=sumlist[-1]
for i in range (min,max+1) :
    if sumlist.count(i)!=0:
        print("The words with ", i ,"letters are:", sumlist.count(i))
