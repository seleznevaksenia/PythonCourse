def count_holes(n):
  
 d={"0":1,"4":1,"6":1,"8":2,"9":1}
 
 counter=0
 
 if isinstance(n,str) and len(n)>0:
   
  l=len(n)-1
 
  n1=n[1:]
  
  n2=n[:l]
  
  n3=n[1:l]
  
  if n.isdigit():
  
   n=str(int(n))
  
   for letter in n:
	
    counter=d.get(letter,0)+counter	
   
   return counter 
	
  elif n[0]=="-" and n1.isdigit():
   
   n=str(int(n1))
	
   for letter in n:
	
    counter=d.get(letter,0)+counter	
   
   return counter
	
  elif n[l]=="L" and n2.isdigit():
   
   n=str(int(n2))
	
   for letter in n:
	
    counter=d.get(letter,0)+counter	
   
   return counter
	
  elif n[0]=="-" and n[l]=="L" and n3.isdigit():
   
   n=str(int(n3))
	
   for letter in n:
	
    counter=d.get(letter,0)+counter	
   
   return counter 	
	
  else:

   return """ERROR"""
 
 elif isinstance(n,int) or isinstance(n,long):
  
  n=str(n)
   
  for letter in n:
	
   counter=d.get(letter,0)+counter	
   
  return counter 
   
 else:

  return """ERROR"""