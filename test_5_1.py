def clean_list(list_to_clean):

 i=0
 
 b=0
 
 while b<len(list_to_clean)-1:
 
  while i<len(list_to_clean)-1:
  
   if (list_to_clean[b]==list_to_clean[i+1]) and (type(list_to_clean[b])==type(list_to_clean[i+1])):
  
    del list_to_clean[i+1]
	
   else:
    
    i=i+1 	
	
  b=b+1

  i=b  
  
 return list_to_clean 