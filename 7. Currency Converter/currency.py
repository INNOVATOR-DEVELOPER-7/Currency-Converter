from tkinter import *
from tkinter import ttk
import requests
import json

con = Tk()
con.title("Currency Converter")
con.geometry("500x530")
con.configure(bg="spring green")
con.resizable(0,0)

frame1 = Frame(con,height=100,width=500,bg= 'steel blue')
frame1.place(x=0,y=0)

L1 = Label(frame1,text='Currency Conveter',font=("Britannic Bold",40,'bold'))
L1.config(bg= "steel blue",fg= "white")
L1.place(x=20,y=20)

F2 = Frame(con,height=80,width = 500,bg='red')
F2.place(x=0,y=450)

L2 = Label(F2,text="",font=("Britannic Bold",15,'bold'))
L2.config(bg="red",fg="white")
L2.place(x =10,y= 20)

from_currency_label = Label(con, text='From', font=('Impact 25 bold'), justify=LEFT)
from_currency_label.config(bg="spring green")
from_currency_label.place(x=5, y=100)

to_currency_label = Label(con, text='To', font=('Impact 25 bold'), justify=RIGHT)
to_currency_label.config(bg="spring green")
to_currency_label.place(x=260, y=100)


amount_label = Label(con, text='AMOUNT', font=('Impact 30 bold'))
amount_label.config(bg="spring green")
amount_label.place(x=155, y=200)

amount_entry = Entry(con, width=8, font=('Poppins 30 bold'))
amount_entry.place(x=15, y=260)

result_label = Label(con, text='', font=('Poppins 15 bold'))
result_label.config(bg="spring green")
result_label.place(x=235, y=260)

API_KEY = "b1b6644b7c33da9f98949f67"
url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD'
response = requests.get(f'{url}').json()
currencies = dict(response['conversion_rates'])

from_currency_combo = ttk.Combobox(con, values=list(currencies.keys()),width=6, font=('Poppins 30 bold'))
from_currency_combo.place(x=20, y=145)

to_currency_combo = ttk.Combobox(con, values=list(currencies.keys()), width=6, font=('Poppins 30 bold'))
to_currency_combo.place(x=280, y=145)

def convert_currency():
    
    source = from_currency_combo.get()
    destination = to_currency_combo.get()
    amount = amount_entry.get()
    
    result = requests.get(f'https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{source}/{destination}/{amount}').json()
    
    converted_result = result['conversion_result']
    
    formatted_result = f'{amount} {source} = {converted_result} {destination}'
    
    result_label.config(text=formatted_result)
    
    L2.config(text='Last updated,' + result['time_last_update_utc'])

convert_button = Button(con, text="CONVERT", bg='gold', fg='white', font=('Impact 25 bold'),command= convert_currency)
convert_button.place(x=155, y=335)

con.mainloop()