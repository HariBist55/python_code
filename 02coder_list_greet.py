f =open("coder_list.txt","r")
names = f.readlines()
for i in range (len(names)):
    names[i] = names[i].strip("\n")
def greet(name):
    print(f"hello good morning:\t{name}")
for coder in names:
    greet(coder)