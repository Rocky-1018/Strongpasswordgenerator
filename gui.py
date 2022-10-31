
from tkinter import *
from winreg import DeleteValue
import Strongpasswordgen
counter_generate=0

def generate():
    global counter_generate
    if(counter_generate==0):
        counter_generate=1
        # clearing previous password once generate button is pressed
        generated_password.delete(0,END)
        num=password_le.get()
        gen_password=Strongpasswordgen.passwo(int(num))
        generated_password.insert(0,gen_password)
        # writing the password to the file which can be used to get hold of passwords in future
       
        with open("passwords.csv","a")as password:
            password.write(platform_entry.get()+","+ gen_password+"\n")
       
def reset():
    generated_password.delete(0,END)
    platform_entry.delete(0,END)
    password_le.delete(0,END)
    global counter_generate
    counter_generate=0


    

window=Tk()
window.title("Strong Password Generator")
window.geometry("500x500")


# label
Heading1=Label(text="Making passwords Strong",font=("Times",30),pady="30px")
Heading1.pack()
platform=Label(text="Password is for :",padx="2px",font=("10"))
platform.place(x=30,y=150)
pass_gen=Label(text="Password-Generated",font=(30),pady="20px")
pass_gen.place(x=30,y=260)
password_len=Label(text="length of password :",font=30)
password_len.place(x=30,y=200)
#entries
platform_entry=Entry(font=25)
platform_entry.place(x=250,y=157)
password_le=Entry(text="",font=10,)
password_le.place(x=250,y=200)
generated_password=Entry(font=25)
generated_password.place(x=240,y=290)


# buttons
bt_generate=Button(text="Generate and save",command=generate)
bt_generate.place(x=250,y=250)
bt_reset=Button(text="Reset for other domain",command=reset)
bt_reset.place(x=250,y=320)

window.mainloop()