import sys

n = sys.argv[1]

num1 = 0

while num1 > -1:

  num1 = n.find("()")
  
  if num1>=0:
  
   n = n.replace("()","")
   
if len(n) == 0:
 
 print "YES"

else:
 
 print "NO" 
 