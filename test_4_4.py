import sys

X1 = int(sys.argv[1])

X2 = int(sys.argv[2])

X=[]

i=0

bilet = 0

for  i in range(1000000):

 X.append(i)

 if len(str(X[i]))<6:
 
  while len(str(X[i]))< 6:
 
   X[i]="0"+str(X[i])
   
 else:
  
  X[i]=str(X[i])
  
for element in X[X1:X2+1]:

 if int(element[0])+int(element[1])+int(element[2])== int(element[3])+int(element[4])+int(element[5]):
  
  bilet = bilet+1  
  
print bilet