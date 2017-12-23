class Student(object):
 labs= []
 name =''
 conf={}
 sum_mark = result = exam =0

 def __init__(self, name, conf):
       
  self.name = name
  self.conf = conf
  self.labs= [0]*self.conf['lab_num']
  

 def make_lab(self,m,n=None):
 
  if n == None:
  
   if 0 in self.labs:
    
	n = self.labs.index(0)
	
   else:
   
    return self
 
  if m > self.conf['lab_max']:
  
   m = self.conf['lab_max']
        
  if n >= self.conf['lab_num']:	

	return self

  self.labs[n] = float(m)
   
  return self

 def make_exam(self,m):
 
  if m > self.conf['exam_max']:
  
   self.exam = self.conf['exam_max']
   
  else:

   self.exam = m 
  
  return self

 def is_certified(self):
 
  self.sum_mark = self.result=0
 
  for elements in self.labs:
  
   self.sum_mark = self.sum_mark+float(elements)
   
  self.result =  float(self.sum_mark) + float(self.exam)
  
  if self.result >= (self.conf['lab_max']*self.conf['lab_num']+self.conf['exam_max'])*self.conf['k']:
  
   return (float(self.result),True,) 
   
  else:

   return (float(self.result),False,)


conf1 ={'exam_max': 20,'lab_max': 40,'lab_num': 2,'k': 0.75} 
o5 = Student('Oleg',conf1)
o5.make_lab(40).make_lab(7,5).make_lab(1).make_lab(7).make_lab(7).make_lab(7).make_lab(7,1).make_lab(7)



   


