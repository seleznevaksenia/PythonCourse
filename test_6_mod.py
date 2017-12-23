def convert_n_to_m(x, n, m):

 lengh=l=result10=ostatok=0
 
 celoe = int
 
 result = ostatok_=''
 
 sys_more10={
    "A" : "10", 
    "B" : "11", 
    "C" : "12", 
    "D" : "13", 
    "E" : "14", 
    "F" : "15", 
    "G" : "16", 
    "H" : "17", 
    "I" : "18", 
    "J" : "19", 
    "K" : "20", 
    "L" : "21", 
    "M" : "22", 
    "N" : "23", 
    "O" : "24", 
    "P" : "25", 
    "Q" : "26", 
    "R" : "27", 
    "S" : "28", 
    "T" : "29", 
    "U" : "30", 
    "V" : "31", 
    "W" : "32", 
    "X" : "33", 
    "Y" : "34", 
    "Z" : "35"}
 if (isinstance(x,str) and x[0]<>"-") or (isinstance(x,int)  and x>=0 ) or (isinstance(x,long)  and x>=0 ):
 
  if (isinstance(x,int) and n<>10):
  
   lengh = len(str(x))
   
   x = str (x)
 
  if (isinstance(x,str) and n<>10):
  
   if x.isalpha() and n <= 9:
   
    return False
  
   x= x.upper()
  
   lengh = len(x)
   
  if (n<>10):
 
   for element in x:
  
    if (element in sys_more10.keys()) and n>10 and (int(sys_more10.get(element)) < n):
   
     element = int (sys_more10.get (element))
  
    elif x.isdigit():
	
	 element = int(element)
	 
    else:
   
     return False   
   
    result10 = result10+ element*(n**(lengh-1))
   
    lengh = lengh -1
  
    if element >  n :
   
     return False

 else:

  return False 
  
 if n == m:
 
  return int(x)
  
 elif (m==1) and (n<>10):
   
  return "0"*result10 
   
 elif (m==1) and (n==10):
  
  return "0"*int(x)
  
 elif n == 10:
 
  if isinstance(x,str):
   
   if (x[len(x)-1]== "L"):
  
    l = len (x)-2 
   
    if not x[0:l].isdigit():
   
     return False
	
    else:
   
     x= long(x) 
	 
   elif x.isdigit():
   
    x= int(x)
   
  while celoe > 0:
  
   if (m > 10) and (str(x%m) in sys_more10.values()):
   
    for key,value in sys_more10.iteritems():

     if value ==  str(x%m):
   
      ostatok_ = key
	
    result = ostatok_ + result
	
   else:	
   
    ostatok = x%m
  
    result = str(ostatok) + result
   
   celoe = x//m
   
   x = celoe
   
  return result 
 
 elif (n <> 10) and (m == 10):
 
  return result10 
 
 else:
 
  x = result10
 
  while celoe > 0:
   
   if (m > 10) and (str(x%m) in sys_more10.values()):
   
    for key,value in sys_more10.iteritems():

     if value ==  str(x%m):
   
      ostatok_ = key
	
    result = ostatok_ + result
	
   else:
	
    ostatok = x%m
  
    result = str(ostatok) + result
    
   celoe = x//m
   
   x = celoe
   
  return result 
  
print convert_n_to_m('ZZZZ', 36, 13)