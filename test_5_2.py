def counter(a,b):
 
 a=str(a)
 
 a1=[]
 
 b=str(b)
 
 b1=[]

 i=x=0
 
 for letter in a:
 
  a1.append(letter)
  
 a1=list(set(a1))
  
 for letter in b:
 
  b1.append(letter)
  
 b1=list(set(b1))
 
 while i<len(a1):
 
  x=b1.count(a1[i])+x

  i=i+1  
    
 return x
  
  






