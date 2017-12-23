import sys

sentence=sys.argv[1]

key = 'aaaaabbbbbabbbaabbababbaaababaab'

alphabet = 'abcdefghijklmnopqrstuvwxyz'

word=""

i=0

d=0

y=0

kod=""

sentence=sentence.replace(" ","")

long=(len(sentence)//5)*5

for i in range(long):

 if "a"<= sentence[i] <="z":
 
  kod=kod+"a"
  
 else:
  
  kod=kod+"b"
  
 i=i+1

i=0
   
for i in range (len(sentence)//5):
 
 y=key.find(kod[d:(d+5)])
 
 word=word+alphabet[y]
  
 d=d+5
 
print word