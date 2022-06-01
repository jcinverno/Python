# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 20:32:39 2021

@author: jcinv
"""

from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=100, pady=50)


def converter():
    mile_value = float(entry.get())
    km_value = round(mile_value * 1.609)
    convert.config(text=f"{km_value}")

entry = Entry(width=7)
entry.grid(column=1, row=0)

miles = Label(text="Miles")
miles.grid(column=2, row=0)
miles.config(padx=30,pady=30)

km = Label(text="Km")
km.grid(column=2, row=1)

equal = Label(text="is equal to")
equal.grid(column=0, row=1)

convert = Label(text=0)
convert.grid(column=1, row=1)

calculate = Button(text="Calculate", command=converter)
calculate.grid(column=1, row= 2)
calculate.config(padx=10, pady=10)




window.mainloop()