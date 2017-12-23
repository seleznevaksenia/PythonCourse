def super_fibonacci(n, m):
 
 if n<=m:

  return 1
 
 else:
 
  sum=0
   
  for i in range (1,m+1):
  
   previous = super_fibonacci(n-i, m)
   
   sum=previous+sum
	
 return sum	
      
print super_fibonacci(8, 2)  

 




