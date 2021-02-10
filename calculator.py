import tkinter as tk
window=tk.Tk()
window.geometry("312x280")
# prevent the window from getting resized
window.resizable(0,0)
window.title("Calculator")

def btn_click(item):
    global expression 
    expression = input_text.get()
    expression =  expression + str(item)
    input_text.set(expression)
def btn_clear():
    global expression
    expression=""
    input_text.set("")
def btn_equal():
    global expression
    expression = input_text.get()
    if expression != "":
        result=str(eval(expression))
        input_text.set(result)
        expression=input_text.get()

expression=""
input_text=tk.StringVar()

input_frame=tk.Frame(window,width=312,height=50,bd=0,highlightbackground="black",highlightcolor="black",highlightthickness=1)
input_frame.pack(side="top")
input_field=tk.Entry(input_frame,font=("arial",18,"bold"),textvariable=input_text,width=50,justify="right")
input_field.pack(ipady=10)
btns_frame=tk.Frame(window,width=312,height=230,bg='grey')
btns_frame.pack()

clear=tk.Button(btns_frame, text = "C", command=lambda : btn_clear(), fg = "black", width = 33, height = 2, bd = 0, bg = "#eee", cursor = "hand2").grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
divide=tk.Button(btns_frame, text = "/", command=lambda : btn_click("/"), fg = "black", width = 10, height = 2, bd = 0, bg = "#eee", cursor = "hand2").grid(row = 0, column = 3, padx = 1, pady = 1)

seven=tk.Button(btns_frame, text = "7", command=lambda : btn_click("7"), fg = "black", width = 10, height = 2, bd = 0, bg = "#fff", cursor = "hand2").grid(row = 1, column = 0, padx = 1, pady = 1)
eight=tk.Button(btns_frame, text = "8", command=lambda : btn_click("8"), fg = "black", width = 10, height = 2, bd = 0, bg = "#fff", cursor = "hand2").grid(row = 1, column = 1, padx = 1, pady = 1)
nine=tk.Button(btns_frame, text = "9", command=lambda : btn_click("9"), fg = "black", width = 10, height = 2, bd = 0, bg = "#fff", cursor = "hand2").grid(row = 1, column = 2, padx = 1, pady = 1)
multiply=tk.Button(btns_frame, text = "*", command=lambda : btn_click("*"), fg = "black", width = 10, height = 2, bd = 0, bg = "#eee", cursor = "hand2").grid(row = 1, column = 3, padx = 1, pady = 1)

four=tk.Button(btns_frame, text = "4", command=lambda : btn_click("4"), fg = "black", width = 10, height = 2, bd = 0, bg = "#fff", cursor = "hand2").grid(row = 2, column = 0, padx = 1, pady = 1)
five=tk.Button(btns_frame, text = "5", command=lambda : btn_click("5"), fg = "black", width = 10, height = 2, bd = 0, bg = "#fff", cursor = "hand2").grid(row = 2, column = 1, padx = 1, pady = 1)
six=tk.Button(btns_frame, text = "6", command=lambda : btn_click("6"), fg = "black", width = 10, height = 2, bd = 0, bg = "#fff", cursor = "hand2").grid(row = 2, column = 2, padx = 1, pady = 1)
minus=tk.Button(btns_frame, text = "-", command=lambda : btn_click("-"), fg = "black", width = 10, height = 2, bd = 0, bg = "#eee", cursor = "hand2").grid(row = 2, column = 3, padx = 1, pady = 1)

one=tk.Button(btns_frame, text = "1",command=lambda : btn_click("1"),  fg = "black", width = 10, height = 2, bd = 0, bg = "#fff", cursor = "hand2").grid(row = 3, column = 0, padx = 1, pady = 1)
two=tk.Button(btns_frame, text = "2",command=lambda : btn_click("2"),  fg = "black", width = 10, height = 2, bd = 0, bg = "#fff", cursor = "hand2").grid(row = 3, column = 1, padx = 1, pady = 1)
three=tk.Button(btns_frame, text = "3",command=lambda : btn_click("3"),  fg = "black", width = 10, height = 2, bd = 0, bg = "#fff", cursor = "hand2").grid(row = 3, column = 2, padx = 1, pady = 1)
plus=tk.Button(btns_frame, text = "+",command=lambda : btn_click("+"),  fg = "black", width = 10, height = 2, bd = 0, bg = "#eee", cursor = "hand2").grid(row = 3, column = 3, padx = 1, pady = 1)

zero=tk.Button(btns_frame, text = "0",command=lambda : btn_click("0"),  fg = "black", width = 22, height = 2, bd = 0, bg = "#fff", cursor = "hand2").grid(row = 4, columnspan=2, padx = 1, pady = 1)
point=tk.Button(btns_frame, text = ".",command=lambda : btn_click("."),  fg = "black", width = 10, height = 2, bd = 0, bg = "#eee", cursor = "hand2").grid(row = 4, column = 2, padx = 1, pady = 1)
equal=tk.Button(btns_frame, text = "=",command=lambda : btn_equal(),  fg = "black", width = 10, height = 2, bd = 0, bg = "#eee", cursor = "hand2").grid(row = 4, column = 3, padx = 1, pady = 1)
window.bind("<Return>",lambda event: btn_equal())

window.mainloop()
