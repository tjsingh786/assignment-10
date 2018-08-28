#ques 1
f2=open("t1.txt",'r')
d=f2.read()
print(d)
f2.close()
print()

#ques 2
f=open("t2.txt",'r')
data=f.read()
w=data.split()
di={}
for word in w:
    di[word]=w.count(word)
print(di)
f.close()
print()

#ques 3
f=open("t1.txt",'r')
line=f.readlines()
for l in line:
    f1=open("t3.txt",'a')
    f1.write(l)
    f1.close()
f.close()
print()

#ques 4
f=open("t1.txt",'r')
f1=open("t3.txt",'r')
for l1,l2 in zip(f,f1):
    f2=open("t4.txt",'a')
    f2.write(l1+l2)
    f2.close()
f.close()
f1.close()
print()

#Que5
with open('t5.txt','w') as f:
   for i in range(10):
      x=int(input("Enter number: "))
      f.write("%d "%(x))

with open('t5.txt','r') as f:
   data=f.readlines()
   for no in data:
       a=no.split()
   a.sort()

with open('t6.txt','w') as f:
   for i in a:
      f.write("%s "%(i))
