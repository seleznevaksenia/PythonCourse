def find_fraction(summ):

 if summ < 3 or summ % 1 != 0:
  return False
  
 if(summ%2 == 0):
  a = summ / 2 - 1
  b = summ / 2 + 1
 else:
  a = (summ - 1)/ 2 
  b = (summ + 1)/ 2
  
 i = 2
 if i <= a: 
  while i <= a:
   a1 = a % i
   b1 = b % i
   if a1 == 0 and b1 == 0:
    a = a/i
    b = b/i
   i = i + 1 
   
 return (int(a),int(b),) 
  
print (find_fraction(2)) # False
print (find_fraction(3)) # (1, 2)
print (find_fraction(10)) # (3, 7)
print (find_fraction(62)) # (29, 33)
print (find_fraction(150000001)) # (75000000, 75000001)