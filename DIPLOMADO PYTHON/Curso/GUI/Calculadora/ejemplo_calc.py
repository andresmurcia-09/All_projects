from tkinter import *

def on_button_click(event):
    button_text = event.widget.cget('text')

    if button_text == '=':
        try:
            result = eval(entry.get())
            entry.delete(0,END)
            entry.insert(END, str(result))
        except:
            entry.delete(0,END)
            entry.insert(END, "Error")
    else:
        current_text = entry.get()
        entry.delete(0,END)
        entry.insert(END, current_text + button_text)

root = Tk()
root.title("Calculadora")
#root.iconbitmap("calculadora.ico")
root.config(bg="green")

entry = Entry(root, width=30, borderwidth=5, justify='right', bg="Black", fg="white")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

for button_text in buttons:
    button = Button(root, text=button_text, padx=20, pady=20)
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", on_button_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()