from tkinter import *

root = Tk()

def click(event):
    button_value = event.widget.cget("text")
    
    if button_value == "C":
        displaying.delete(0, END)
    elif button_value == "=":
        try:
            expression = displaying.get()
            result = eval(expression) 
            displaying.delete(0, END)
            displaying.insert(END, str(result))
        except Exception as e:
            displaying.delete(0, END)
            displaying.insert(END, "Error")
    else:
        
        displaying.insert(END, button_value)


root.geometry("700x500")
root.title("Calculator")

name = Label(root, text="Welcome to Saurav Calculator", pady=30, padx=15, fg="red", font=("Lexend", 30))
name.pack()

displaying = Entry(root, font=("Lexend", 15), borderwidth=2, relief="solid", justify="right")
displaying.pack(pady=30, padx=20, fill="x")

def create_button(text, frame):
    btn = Button(frame, text=text, fg="Black", font=("Lexend", 30))
    btn.pack(side=LEFT, padx=5)
    btn.bind("<Button-1>", click)
    return btn

f = Frame(root)
create_button("9", f)
create_button("8", f)
create_button("7", f)
create_button("=", f)
f.pack(pady=5)

f = Frame(root)
create_button("6", f)
create_button("5", f)
create_button("4", f)
create_button("+", f)
f.pack(pady=5)

f = Frame(root)
create_button("3", f)
create_button("2", f)
create_button("1", f)
create_button("-", f)
f.pack(pady=5)

root.mainloop()
