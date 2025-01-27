import tkinter as tk

def calculate():
    total_amount= float(textbox1.get())
    total_person= int(textbox2.get())

    amount_per_person= total_amount/total_person
    result_label.config(text=f"each person need to pay{amount_per_person}:")

root = tk.Tk()
root.title("Hari Bist split software")
 
 #set height width
root.geometry("500x500")


label1=tk.Label(root,text="Enter Total Amount RS:")
label1.pack(pady=10)

textbox1 = tk.Entry(root)
textbox1.pack()

label2=tk.Label(root,text="Enter a person lists :")
label2.pack()

textbox2 = tk.Entry(root)
textbox2.pack(pady=10)


Button1 = tk.Button(root,text="calculate",command=calculate)
Button1.pack()

result_label =tk.Label(root,text=" ")
result_label.pack() 

root.mainloop()