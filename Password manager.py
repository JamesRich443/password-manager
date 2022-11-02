from cgitb import text
from tkinter import *
from tkinter.tix import COLUMN
from turtle import width
from tkinter import messagebox
import random
def save():
    wlf=wl_input.get()
    elf=el_input.get()
    plf=pl_input.get()

    if len(wlf)==0 or len(plf)==0 or len(elf)==0:
        messagebox.showinfo(message="no blank fields")
    else:
        is_ok=messagebox.askokcancel(title=wl_input,message=f"check your entry:\n Email:{el_input}\n password:{pl_input} ")
         
        if is_ok:
            with open("password_manager.txt", "a") as datafile:
                datafile.write(f"{wlf} | {elf} | {plf}\n")  
                wl_input.delete(0,END)
                el_input.delete(0,END)
                pl_input.delete(0,END)
    

def password_generator():
    letters=['a','b','c','d','e','q','w','r','t','y','u','i','o','p',
's','f','g','h','j','k','l','z','x','v','b','n','m']

    nums=['1','2','3','4','5','6','7','8','9','0']

    sc=['!','@','#','$','%','&','*']
    rand_let=[random.choice(letters) for i in range(random.randint(4,8))]
    rand_special=[random.choice(sc) for i in range(random.randint(5,9))]
    rand_nums=[random.choice(nums) for i in range(random.randint(3,5))]
    rand_list=rand_let+rand_special+rand_nums
    random.shuffle(rand_list)
    gener_pass="".join(rand_list)
    pl_input.insert(0,gener_pass)
     

home_page=Tk()
home_page.title("Password Manager")
canvas=Canvas(width= 600, height= 400)

logo=PhotoImage(file="logo.png")
canvas.create_image(300,200,image=logo)
canvas.grid(row=0 ,column=1)
home_page.config(padx=20,pady=20)

wl= Label(text='Website')
wl.grid(row=1,column=0)
el= Label(text='Username')
el.grid(row=2,column=0)
pl= Label(text='password')
pl.grid(row=3,column=0)


wl_input=Entry(width=35)
wl_input.grid(row=1,column=1,columnspan=2)
el_input=Entry(width=35)
el_input.grid(row=2,column=1,columnspan=2)
pl_input=Entry(width=35)
pl_input.grid(row=3,column=1)

   

gp=Button(text="Generate Password",command=password_generator)

gp.grid(row=3,column=2)
ab=Button(text="ADD",width=36,command=save)
ab.grid(row=4,column=1,columnspan=2)
home_page.mainloop()





