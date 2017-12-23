def saddle_point(matrix):
 
 index1=[]
 
 index2=[]
 
 col=i=j=flag=fix=0
 
 col_test=[]
 
 matrix_changebl=matrix
 
 result=()

 for row in matrix:
 
  if row.count(min(row))>1:
  
   fix=min(row)
  
   while fix in row:
    
	col=row.index(min(row))
   
	row.remove(min(row))
	
	row.insert(col,"x")
	
	index1.append((i,col))
  
  else:
  
   col=row.index(min(row))
  
   index1.append((i,col))
  
  i=i+1
  
 i=0 
  
 for j in range(len(matrix_changebl[0])):
 
  for i in range(len(matrix_changebl)):
  
   col_test.append(matrix_changebl[i][j])
   
  if col_test.count(max(col_test))>1:
  
   fix=max(col_test)
   
   while fix in col_test:
  
    col=col_test.index(max(col_test))
   
    col_test.remove(max(col_test))
	
    col_test.insert(col,-1)
	
    index2.append((col,j))
  
  else:
   
   col=col_test.index(max(col_test))
  
   index2.append((col,j))
  
  col_test=[]

  i=0
  
 for element in index1:
 
  if element in index2:
  
   flag=flag+1

   if flag==1:
  
    result = element 
   
 if flag==1:
 
  return result
 
 else:
 
  return False
  
print saddle_point([[1,2,3,0,1,1], [4,3,2,1,1,2], [4,3,2,0,1,1], [0,0,0,0,0,1]])
  
 

