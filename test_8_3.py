def bouquets(narcissus_price, tulip_price, rose_price, summ):

 if summ == 0:
  return 0
 prices=sorted([narcissus_price, tulip_price, rose_price])
 i = 0
 j = 0
 k = 0
 max = summ/prices[2]
 middle = summ/prices[1]
 min = summ/prices[0]
 quontity = 0
 
 while k <= min:
  while j <= middle:
   while i <= max:
    i= i+1
    if prices[2]*i+prices[1]*j+prices[0]*k <= summ and (i+j+k)%2 != 0:
     quontity = quontity+1
   i = 0	 
   j= j+1
   if prices[2]*i+prices[1]*j+prices[0]*k <= summ and (i+j+k)%2 != 0:
    quontity = quontity+1
  j = 0
  k = k +1
  if prices[2]*i+prices[1]*j+prices[0]*k <= summ and (i+j+k)%2 != 0:
   quontity = quontity+1
 
   
 return quontity 
  
print (bouquets(3,4,5,3) ) # 34
print (bouquets(2,3,4,10)) # 12
print (bouquets(2,3,4,100)) # 4019
print (bouquets(200,300,400,10000)) # 4019
print (bouquets(200,300,400,100000)) # 3524556