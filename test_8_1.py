class CombStr(object):
       
 def __init__(self, string):
       
  self.string = string

 def count_substrings(self,length):
  n = len(self.string)
  i = 0
  my_list = []
  if(length == 0 or length > n):
   return 0
  elif (length == n):
   return 1
  else:
   while i != (n - length):
    i = i+1
    if(self.string[i:length+i] not in my_list):
     my_list.append(self.string[i:length+i])
    else:
     continue
	 
  return len(my_list)
		
s0 = CombStr('qqqqqqweqqq%')
print (s0.count_substrings(0)) # 0
print (s0.count_substrings(1)) # 4
print (s0.count_substrings(2)) # 5
print (s0.count_substrings(5)) # 7
print (s0.count_substrings(15)) # 0