from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

l=list()
print(logo)
slot=dict()
auct=True
while auct:
  name=input(" Input Name:  ")
  price=input("Whats your Bid Price:  ")
  
  slot[name]=price  
  
  opt=input("Any more users: ")
  if opt =="yes":
    clear()
  else:
    auct=False
    
  
  for pop in slot:
    
    l.append(slot[pop])
   
j=max(l)
print("max is "+j)
for key,value in slot.items():
  if j==value:
    print(f"The Bidder is +{key}")
        
    
    
    
  