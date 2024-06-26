import tkinter
import requests
from bs4 import BeautifulSoup

# Currency conversion function
def printfunction():
    # error handling incase there is an error due to invalid inputs
    try:
        amount_str = amount_entry.get()
        from_str = from_entry.get()
        to_str = to_entry.get()
        # extraction of real time currency exchange values from "www.xe.com"
        x=requests.get(f"https://www.xe.com/currencyconverter/convert/?Amount={amount_str}&From={from_str}&To={to_str}")
        soup = BeautifulSoup(x.content,"html.parser")
        rate=soup.find(class_="result__BigRate-sc-1bsijpp-1 iGrAod")
        converted_str = rate.get_text()
        # creates a label that prints the converted value
        converted = tkinter.Label(mainwindow,text=f"{amount_str} {from_str} = {converted_str} {to_str}")
        converted.place(x=0,y=340,width=500)
        converted.configure(font=("serif",23,"bold"),bg="black",fg="green")
    except:
        # creates a label which prints an error for invalid input.
        error_label = tkinter.Label(mainwindow,text=f"Error ! Invalid currency inputs.")
        error_label.place(x=0,y=340,width=500)
        error_label.configure(font=("serif",23,"bold"),bg="black",fg="green")

#The main GUI window
mainwindow = tkinter.Tk()
mainwindow.title("Currency Converter") 
mainwindow.configure(bg="black")
mainwindow.geometry("500x400")
logo = tkinter.PhotoImage(file="Currencyconverter.png") # Logo image
# Placing logo image in the main window
CC = tkinter.Label(mainwindow,image=logo)
CC.place(x=0,y=0,width=500,height=230)
CC.configure(font=("fixedsys",40),bg="black",fg="green")
# "amount" "from" "to" row creation in main window
amount = tkinter.Label(mainwindow,text="AMOUNT:",fg="green",bg="black",font=("serif",14,"bold")) # Label of "amount"
amount.place(x=20,y=250)
textx=tkinter.StringVar() # amount input is stored in this variable
textx.set("1") # default amount-variable value
amount_entry = tkinter.Entry(mainwindow,textvariable=textx) # amount input box
amount_entry.place(x=95,y=250,height=25,width=60)


def fromsetfunction(x):
    from_input.set(x)

def tosetfunction(x):
    to_input.set(x)


    
# drop down menu arrow image
arrow = tkinter.PhotoImage(file='arrow.png')

from_currency = tkinter.Label(mainwindow,text="FROM:",fg="green",bg="black",font=("serif",14,"bold")) # Label of "from"
from_currency.place(x=170,y=250)

# From input
from_input=tkinter.StringVar() # variable to store "from" input
drop_from = tkinter.OptionMenu(mainwindow,from_input,"INR","USD","EUR","CNY","AUD","JPY","NZD","GBP","CAD",command=fromsetfunction) # drop down menu of currencies
drop_from.place(x=282,y=255,width=35,height=15)
drop_from.config(image=arrow,bg="black")
from_entry = tkinter.Entry(mainwindow,textvariable=from_input) # type-written input box for currency
from_entry.place(x=230,y=250,height=25,width=60)

# To input
to_currency = tkinter.Label(mainwindow,text="TO:",fg="green",bg="black",font=("serif",14,"bold")) # Label of "to"
to_currency.place(x=340,y=250)
to_input = tkinter.StringVar() # variable to store "to" input
drop_to = tkinter.OptionMenu(mainwindow,to_input,"INR","USD","EUR","CNY","AUD","JPY","NZD","GBP","CAD",command=tosetfunction) # drop down menu of currencies
drop_to.place(x=432,y=255,width=35,height=15)
drop_to.config(image=arrow,bg="black")
to_entry = tkinter.Entry(mainwindow,textvariable=to_input) # type-written input box for currency
to_entry.place(x=380,y=250,height=25,width=60)

convert_button_image = tkinter.PhotoImage(file="convert.png") # convert button image
# convert button
convert_button = tkinter.Button(mainwindow,image=convert_button_image,command=printfunction,bg="black")
convert_button.place(x=200,y=300,height=30,width=102)
mainwindow.mainloop()