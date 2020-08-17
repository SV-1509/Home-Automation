import os
list=[]
with open('numbers.txt','r') as filehandle:
	for line in filehandle:
		number=line[:-1]
		list.append(number)
list1=[]		
for i in range(len(list)):
	list1.append(int(list[i]))	
print(list1)
import matplotlib.pyplot as plt
import random

v=0
x=[]
y=[]
k=[]
p=[]
n=[]
g=[]
print(len(list1))
for i in range(60):
 # l =random.randint(1,5)
 # y.append(l)
  y.append(list1[i])
  v=v+4
  x.append(v)

for t in range(10):
	k.append(0)
	n.append(0)
	p.append(t+1)

for j in range(10):
	for i in range(60):
		if ((i+1)<=6*(j+1)):

			k[j]=k[j]+y[i]

for o in range(10):
	if(o==0):
		n[o]=k[o]
	else:
	 n[o]=k[o]-k[o-1]



m=[1,2,3,4,5,6]
a=y[0]
b=y[1]
c=y[2]
d=y[3]
e=y[4]
f=y[5]
o=len(y)/6
for i in range(10):
	a=a+y[6*i]/o
	b=b+y[6*i+1]/o
	c=c+y[6*i+2]/o
	d=d+y[6*i+3]/o
	e=e+y[6*i+4]/o
	f=f+y[6*i+4]/o
g.append(a)
g.append(b)
g.append(c)
g.append(d)
g.append(e)
g.append(f)

plt.subplot(211)
plt.bar(m,g)
plt.title("Average Hourly Consumption")
plt.ylabel("No of Units")
plt.xlabel("Time intervals")
plt.subplot(212)
plt.bar(p,n)
plt.title("Daily Consumption")
plt.ylabel("No of Units")
plt.xlabel("Day")
plt.savefig('g.png')
os.system("sudo cp g.png /var/www/html")
plt.show()
    
   
   





