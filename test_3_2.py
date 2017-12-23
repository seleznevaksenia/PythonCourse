import sys

n = int(sys.argv[1])

feb1 = 0

feb2 = 1

i = 0

x = 0

febn = 0

if n==0:

 print feb1

elif n == 1:

 print feb2
 
else:

 while i < (n-1):

  febn = feb1+feb2
 
  x = feb2
 
  feb1 = x
  
  feb2 = febn
   
  i = i+1

 print febn
  
