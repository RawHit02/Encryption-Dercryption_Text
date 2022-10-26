from tkinter import *
from tkinter import messagebox
import base64

screen = Tk()
screen.geometry("420x420")
screen.title("Encryption & Decryption ")
screen.configure(bg="Black")

def encrypt():
    password=code.get()
    if password=="123456":
        screen1=Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x250")
        screen1.configure(bg="LavenderBlush")
        
        message=text1.get(1.0,END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")
        
        Label(screen1,text="⭐ Code Is ENCRYPTED ✔",font="impack 16 bold",fg="MediumSlateBlue",bg="LavenderBlush").place(x=5,y=6)
        text2= Text(screen1,font="30",bd=4,wrap=WORD)
        text2.place(x=2,y=40,width=390,height=180)
        text2.insert(END,encrypt)
        
    elif(password==""):
       messagebox.showerror("❌ Error !","Please Enter Secret Key")
    elif(password!="123456"):
        messagebox.showerror("❌ OOPS !","Invalid Secret Key") 
        
def decrypt():
    password=code.get()
    if password=="123456":
        screen2=Toplevel(screen)
        screen2.title("Encryption")
        screen2.geometry("400x250")
        screen2.configure(bg="LavenderBlush")
        
        message=text1.get(1.0,END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(encode_message)
        encrypt = base64_bytes.decode("ascii")
        
        Label(screen2,text="⭐ Code Is DECRYPTED ✔",font="impack 16 bold",fg="MediumSlateBlue",bg="LavenderBlush").place(x=5,y=6)
        text2= Text(screen2,font="30",bd=4,wrap=WORD)
        text2.place(x=2,y=40,width=390,height=180)
        text2.insert(END,encrypt)
        
    elif(password==""):
       messagebox.showerror("❌ Error !","Please Enter Secret Key")
    elif(password!="123456"):
        messagebox.showerror("❌ OOPS !","Invalid Secret Key") 
        
def reset():
    text1.delete(1.0,END)
    code.set("")
    
#label
Label(screen,text="Enter Text To ENCRYPT and DECRYPT 👇🏽",font="arial 14 bold",bg="Black",fg="Azure").place(x=5,y=6)

#Text
text1=Text(screen,font="20",bg="LavenderBlush")
text1.place(x=5,y=45,width=410,height=120)
#Label
Label(screen,text="Enter Secret Key 🗝",font="impack 14 bold",bg="Black",fg="Red").place(x=120,y=185)
#entry
code=StringVar()
Entry(textvariable=code,bd=4,font="20",show="*",bg="LavenderBlush").place(x=95,y=220) 
#button
Button(screen,text="Encrypt 🔒",font="arial 15 bold",bg="LavenderBlush",fg="Green",command=encrypt).place(x=30,y=280,width=160)
Button(screen,text="Decrypt 🔐",font="arial 15 bold",bg="LavenderBlush",fg="Green",command=decrypt).place(x=235,y=280,width=160)
Button(screen,text="Reset ♻",font="arial 15 bold",bg="LavenderBlush",fg="DodgerBlue",command=reset).place(x=90,y=350,width=240)
mainloop()