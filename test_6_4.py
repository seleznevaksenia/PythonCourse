def find_most_frequent(text):

 znaki=[",",".",":",";","!","?","-","-"]
 
 new_text=result=[]
 
 result_dict={}
 
 text= text.lower()
 
 n=s=0

 for element in znaki:
 
  if text.find(element)<>-1:
 
   text=text.replace(element," ")   # Replace all punctuation marks on " "
 
  for element in text:
  
   if element == " ":
   
    n=n+1
	
   else:

    if n>=2:

     text=text.replace(" "*n," ")  # Raplace more than 1 space by 1 space
	 
     n=0

 text=text.strip(" ") 
 
 new_text=text.split(" ")
 
 new_text=sorted(new_text)
 
 while s<len(new_text):
 
  if new_text.count(new_text[s])>1:
  
   result_dict[new_text[s]]=new_text.count(new_text[s]) # Create dict like = {word : amount of repeat}
   
   s=s+new_text.count(new_text[s])
   
  else: 

   s=s+1    
   
 for key,value in result_dict.iteritems():

  if value ==  max(result_dict.values()):
   
   result.append(key) # Create list of the keys of max value
   
 return sorted(result)
 
