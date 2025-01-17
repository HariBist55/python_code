# Create 3 Lucky Winner From names.txt file using Random.

import random
name =["Som Prakash Chaudhary","Nishan Poudel","Shankarsan Khadka","Raj Poudel","Deepak Prasad Poudel","Hari Bist","Dilip Karki",
       "Tolak Raj Chapagain","Padam Bahadur Rai""Kishor Saud","Aakriti Rai","Diwash Sharma Acharya","Suresh Koli","Pujana Banstola",
       "Nitesh Bishwokarma","Binay Shrestha","Mani thapa""Kiran paudel","Surendra shakya"]


winner1 =random.choice(name)
print(f"1st LUCKY WINNER from names:{winner1}")
name.remove(winner1)                                

winner2 = random.choice(name)
print(f"2nd Lucky WINNER from Name:{winner2}")
name.remove(winner2)

winner3 = random.choice(name)
print(f"3rd LUCKY WINNER from name:{winner3}")
name.remove(winner3)
