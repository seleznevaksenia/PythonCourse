import sys
 
x = [] 

sum = ''

x = sys.argv[::-1]

x.pop()

for arg in x[::1]:

 sum = sum + str(arg)+' '
 
print sum.rstrip(' ')