# Top 15 Players for the Men's Ballon d'Or
f = open("football.txt","r")
names = f.readlines()
for i in range (len(names)):
  names[i] = names [i].strip("\n")
 
names = [r.upper() for r in names]
name = input("enter a player's name: ")
if name.upper()in names:
   print(f"{name} is  in top 15")
else:
   print(f"not available")