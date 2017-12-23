def file_search(folder, filename):

 n=0

 result=""

 x=""
  
 for n in range(len(folder)):
  
  if (isinstance(folder[n], str)) and (folder[n] == filename):
   
   result = str(folder[0])+"/"+str(folder[n])
   
   break
	 
  elif (isinstance(folder[n], str)) and (folder[n] != filename):
   
   if n==(len(folder))-1:
   
    result=False
	
  elif  isinstance(folder[n], list):
  
   x=file_search(folder[n], filename)
   
   if x<>False:
   
    result=str(folder[0])+"/"+x
	
    break
	
   elif (x==False)	and (n==(len(folder))-1):
   
    result=False
   
 if result<>False:

  return  result

 else:

  return False  
	  	  
print file_search(['D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me']], 'hey.py'], 'find.me')