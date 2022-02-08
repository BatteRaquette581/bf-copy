from sys import *
a=[]
for i in range(9999):a.append(0)
f=open("bfCopy.txt","r").read()
def p(m):
 global c
 c=0
 w=""
 l=0
 for i in m:
  if c>9999:c=9999
  if c<0:c=0
  if i=="(":
   l=1
   continue
  if i==")":
   l=0
   while a[c]!=0:p(w)
  if l:
   w+=i
   continue
  if i=="^":c+=1
  if i=="v":c-=1
  if i=="i":a[c]+=1
  if i=="d":a[c]-=1
  if i=="!":stdout.write(chr(a[c]))
  if i=="?":a[c]=int(input())
  if i=="§":stdout.write(str(a[c]))
  if i=="m":stdout.write(str(a))
p(f)