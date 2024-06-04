# -*- coding: utf-8 -*-
"""
Created on Thu May 30 17:12:34 2024

@author: bacht
"""

import pickle
# Import Module
from tkinter import *
# load the model
model = pickle.load(open("lrsaham2.pkl", "rb"))


 
# create root window
root = Tk()
 
# root window title and dimension
root.title("BBTN Stock Price Predictor")
# Set geometry (widthxheight)
root.geometry('350x200')

lbl_nim = Label(root, text = "Net Interest Rate (in %)")
lbl_nim.grid()
txt_nim = Entry(root, width=10)
txt_nim.grid(column =1, row =0)

lbl_npl = Label(root, text = "Non Performing Loan (in %)")
lbl_npl.grid()
txt_npl = Entry(root, width=10)
txt_npl.grid(column =1, row =1)

lbl_birate = Label(root, text = "BI Rate (in %)")
lbl_birate.grid()
txt_birate = Entry(root, width=10)
txt_birate.grid(column =1, row =2)

def clicked(event=None):
    result=[txt_nim.get(),txt_npl.get(),txt_birate.get()]
    result2=[]
    for i in result:
        if "," in i:
            result2.append(float(i.replace(",",".")))
        else:
            result2.append(float(i))
            
    Y_pred = model.predict([result2])
    
    lbl_result = Label(root, text = "The price after 3 month is "+str(round(Y_pred[0])))
    lbl_result.grid()


#button widget with red color text
# inside
btn = Button(root, text = "Result" ,
             fg = "red", command=clicked)
root.bind('<Return>', clicked)
# set Button grid
btn.grid(column=1, row=3)
# all widgets will be here
# Execute Tkinter
root.mainloop()
#https://www.youtube.com/watch?v=b2rPqPZ8was