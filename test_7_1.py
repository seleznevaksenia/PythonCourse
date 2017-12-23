import math
class Sphere(object):
       
 def __init__(self, rad = 1.0, x = 0.0, y = 0.0, z = 0.0):
       
  self.radius = rad
  self.koord_x = x
  self.koord_y = y
  self.koord_z = z

 def get_volume(self):
        
  return float((4*math.pi*math.pow(self.radius,3))/3)

 def get_square(self):

  return  float(4*math.pi*math.pow(self.radius,2))

 def get_radius(self):

   return  float(self.radius)

 def get_center(self):

  return  (float(self.koord_x),float(self.koord_y), float(self.koord_z),)

 def set_radius(self,r):

  self.radius = float(r)

 def set_center(self,x,y,z):
 
  self.koord_x = self.koord_x+x
  self.koord_y = self.koord_y+y
  self.koord_z = self.koord_z+z

 def is_point_inside(self,x,y,z):

  if (math.pow(self.koord_x-x, 2)+math.pow(self.koord_y-y, 2)+math.pow(self.koord_z-z, 2) <= math.pow(self.radius,2)):

   return True
   
  else: 

   return False


