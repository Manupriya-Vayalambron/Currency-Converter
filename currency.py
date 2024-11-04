from currency_converter import CurrencyConverter
import tkinter as tk

a=CurrencyConverter()

def clicked():
    amount = int(e1.get())
    cur1 = e2.get()
    cur2 = e3.get()
    data=round(a.convert(amount,cur1,cur2),2)
    l5=tk.Label(window,text= data,font="Times 17 bold").place(x=225, y=290)


window = tk.Tk()
window.title("Convert From One Currency To Another")
window.geometry("500x360")
l1=tk.Label(window,text="Currency Converter", font="Times 25 bold").place(x=100,y=30)
l2=tk.Label(window,text="Enter amount here: ", font="Times 17 bold" ).place(x=50,y=80)
e1=tk.Entry(window)

l3=tk.Label(window,text="Enter currency: ", font="Times 17 bold" ).place(x=50,y=130)
e2=tk.Entry(window)

l4=tk.Label(window,text="Enter req currency: ", font="Times 17 bold" ).place(x=50,y=180)
e3=tk.Entry(window)

b=tk.Button(window,text="convert",command=clicked).place(x=230,y=240)
e1.place(x=300,y=90)
e2.place(x=300,y=140)
e3.place(x=300,y=190)
window.mainloop()
