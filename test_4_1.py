
import sys

x = ''

text_space = ''

text = sys.argv[1].lower()

text_space = text.replace(' ','')

x = text_space[::-1]

if text_space == x:
	
 print 'YES'

else:
		
 print 'NO'
		
