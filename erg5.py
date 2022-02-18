f=open('two_cities_ascii.txt','r')
lines=f.read()
f.close()
list=('abcdefghijklmnopqrstuvwxyz \nABCDEFGHIJKLMNOPQRSTUVWXYZ')
#makes the capital letter small
answer=''.join(filter(list.__contains__,lines))
answer=answer.lower()
#prints the 10 most popular words in the text
from collections import Counter
find=answer.split()
Counter=Counter(find)
most_occ=Counter.most_common()
most_occwords= Counter.most_common(10)
print ("\n The 10 most popular words in the text are:\n('words',times in the text)\n", most_occwords,"\n\n")
#makes 2 lists
words=[]
words.append(answer)
words=answer.split()
words2=[]
words2.append(answer)
words2=answer.split()
#removes the words with 1 letter
sum1=[]
sum1=[len(i)for i in words]
i=0
while i<len(words):
    if sum1[i]<2:
        sum1.pop(i)
        words.pop(i)
    i+=1
for i in range(0,len(words)):
            words[i]=words[i][0:2]
#prints the 3 most popular combinations of two first letters that words in the text beggin
from collections import Counter
Counter=Counter(words)
most_occ=Counter.most_common(3)
print ("The 3 most popular combinations of two first letters that words in the text beggin are : \n ('words',times in the text)\n",most_occ,"\n\n")
#removes the words with 1 or 2 letters
sum2=[]
sum2=[len(i)for i in words2]
i=0
while i<len(words2):
    if sum2[i]<3:
        sum2.pop(i)
        words2.pop(i)
    i+=1
for i in range (0,len(words2)):
    words2[i]=words2[i][0:3]
#prints the 3 most popular combinations of three first letters thw words in the text beggin
from collections import Counter
Counter=Counter(words2)
most_occ2=Counter.most_common(3)
print ("The 3 most popular combinations of three letters that words in the text beggin are :\n ('words',times in the text)\n",most_occ2,"\n\n")
