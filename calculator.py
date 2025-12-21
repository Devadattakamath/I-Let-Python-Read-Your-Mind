from tkinter import *

expr = ""

def press(key):
    global expr
    expr += str(key)
    display.set(expr)

def equal():
    global expr
    try:
        display.set(str(eval(expr)))
        expr = ""
    except:
        display.set("Error")
        expr = ""

def clear():
    global expr
    expr = ""
    display.set("")

root = Tk()
root.title("Calculator")
root.geometry("360x500")
root.configure(bg="#1e1e1e")
root.resizable(True, True)

# Make grid responsive
for i in range(4):
    root.columnconfigure(i, weight=1)
for i in range(6):
    root.rowconfigure(i, weight=1)

display = StringVar()

entry = Entry(
    root,
    textvariable=display,
    font=("Arial", 26),
    bg="#111",
    fg="white",
    bd=0,
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=15)

def create_btn(text, row, col, cmd, bg="#2e2e2e", colspan=1):
    Button(
        root,
        text=text,
        font=("Arial", 16),
        bg=bg,
        fg="white",
        bd=0,
        command=cmd
    ).grid(
        row=row,
        column=col,
        columnspan=colspan,
        sticky="nsew",
        padx=6,
        pady=6
    )

# Numbers
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2),
    ('4',2,0), ('5',2,1), ('6',2,2),
    ('1',3,0), ('2',3,1), ('3',3,2),
    ('0',4,0), ('.',4,1)
]

for text, r, c in buttons:
    create_btn(text, r, c, lambda x=text: press(x))

# Operators
create_btn('+',1,3, lambda: press('+'), "#ff9500")
create_btn('-',2,3, lambda: press('-'), "#ff9500")
create_btn('*',3,3, lambda: press('*'), "#ff9500")
create_btn('/',4,3, lambda: press('/'), "#ff9500")

# Clear & Equals
create_btn('C',4,2, clear, "#ff3b30")
create_btn('=',5,0, equal, "#34c759", colspan=4)

root.mainloop()
