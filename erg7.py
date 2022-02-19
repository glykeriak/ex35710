import json
f=open("di.txt","r")
c=f.read()
d=c
dic=c.split("\n")
Dict={}
for i in range(len(dic)):
    Dict[i]=json.loads(dic[i])
fltr='abcdefghijklmnopqrstuvwxyz \nABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
d=''.join(filter(fltr.__contains__,d))
f.close()
key=Dict[0].keys()
#prints the available keys
print("Available keys:")
for i in key:
    print(i)
#asks to select a key
select=input("Select a key:")
#prints min and max values
n=Dict[0]
max=n[select]
min=n[select]
for i in range(1,len(Dict)):
    n=Dict[i]
    if max<n[select]:
        max=n[select]
    if min>n[select]:
        min=n[select]
print("Min value:",min,"\n")
print("Max value:",max,"\n")
