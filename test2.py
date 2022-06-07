from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import Tk, StringVar, Label, Entry, Button
from functools import partial

def update_label(label, stringvar):
    """
    Met à jour le texte d'un label en utilisant une StringVar.
    """
    text = stringvar.get()
    label.config(text=text)
    stringvar.set('Merci')
root = Tk()
text = StringVar(root)
label = Label(root, text='What is the desired angle?')

entry_name = Entry(root, textvariable=text)

def askMe():
    if entry_name < 0:
        messagebox.showwarning('error', 'the angle must be between 0 and 180')
    elif entry_name > 180:
        messagebox.showwarning('error', 'the angle must be between 0 and 180')
    else: 
        pass

button = Button(root, text='Go', command=partial(update_label, label, text))

label.grid(column=0, row=0)
entry_name.grid(column=0, row=1)
button.grid(column=0, row=2)

root.mainloop()

from tkinter import *
from tkinter import filedialog as fd 
ws = Tk()
ws.title("Python Guides")
ws.geometry("100x100")
def callback():
    name= fd.askopenfilename() 
    print(name)
    
error_msg = 'Error!'
Button(text='Enregister les mesures', 
       command=callback).pack(fill=X)
ws.mainloop()

def killWin():
	toplevel = Toplevel(ws)

	toplevel.title("Terminer les mesures")
	toplevel.geometry("230x100")


	l1=Label(toplevel, image="::tk::icons::question")
	l1.grid(row=0, column=0)
	l2=Label(toplevel,text="Are you sure you want to Quit")
	l2.grid(row=0, column=1, columnspan=3)

	b1=Button(toplevel,text="Yes",command=ws.destroy, width=10)
	b1.grid(row=1, column=1)
	b2=Button(toplevel,text="No",command=toplevel.destroy, width=10)
	b2.grid(row=1, column=2)


ws = Tk()
ws.geometry("300x200")
ws.title('Python Guides')
ws.config(bg='#345')
Button(ws,text="Terminer les mesures",command=killWin).pack(pady=80)
ws.mainloop()


print("test2")