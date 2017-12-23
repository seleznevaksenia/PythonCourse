import sys

import math

a = float(sys.argv[1])

b = float(sys.argv[2])

c = float(sys.argv[3])

if (a<=0) or (b<=0) or (c<=0):

 print "not triangle"
 
else:

  if (a<(b+c)) and (a>math.fabs(b-c)) and (b<(a+c)) and (b>math.fabs(a-c)) and (c<(a+b)) and (c>math.fabs(a-b)):
	
   print "triangle"

  else:
 
   print "not triangle"