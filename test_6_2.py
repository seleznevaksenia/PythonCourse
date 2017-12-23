def encode_morze(text):

 counter=""
 
 result=""
 
 withoutspace=""
 
 withspace=""
 
 l=0
 
 text=text.upper()
 
 morse_code = {
    "A" : ".-", 
    "B" : "-...", 
    "C" : "-.-.", 
    "D" : "-..", 
    "E" : ".", 
    "F" : "..-.", 
    "G" : "--.", 
    "H" : "....", 
    "I" : "..", 
    "J" : ".---", 
    "K" : "-.-", 
    "L" : ".-..", 
    "M" : "--", 
    "N" : "-.", 
    "O" : "---", 
    "P" : ".--.", 
    "Q" : "--.-", 
    "R" : ".-.", 
    "S" : "...", 
    "T" : "-", 
    "U" : "..-", 
    "V" : "...-", 
    "W" : ".--", 
    "X" : "-..-", 
    "Y" : "-.--", 
    "Z" : "--..",
    " " : "_"}
	
 radio={"-":"^^^",".":"^","_":"_"}
   
 for letter in text:
 
  withoutspace=morse_code.get(letter,"")
  
  if withoutspace<>"":
  
   for letter in withoutspace:
   
    withspace=withspace+letter+"_"

   counter=counter+withspace+"__"
  
   withspace=""

 for letter in counter:

  result=result+radio.get(letter,"")
  
 l=len(result)-3
 
 return result[:l]