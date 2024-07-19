from tkinter import messagebox
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import tkinter as tk
from tkinter import ttk
import time
from datetime import datetime



my_dict = {
    'timestamp': 1721390794.3526573, 
    'data': {'ABD Doları': {'alış': '33,0610', 'satış': '33,0669'}, 
             'Euro': {'alış': '36,0319', 'satış': '36,0458'}, 
             'İngiliz Sterlini': {'alış': '42,7464', 'satış': '42,7722'}, 
             'İsviçre Frangı': {'alış': '37,1597', 'satış': '37,1798'}, 
             'Japon Yeni': {'alış': '0,2106', 'satış': '0,2093'}, 
             'Suudi Arabistan Riyali': {'alış': '8,7816', 'satış': '8,8256'}, 
             'Norveç Kronu': {'alış': '3,0341', 'satış': '3,0494'}, 
             'Danimarka Kronu': {'alış': '4,8075', 'satış': '4,8316'}, 
             'Avustralya Doları': {'alış': '22,0549', 'satış': '22,1655'}, 
             'Kanada Doları': {'alış': '24,0253', 'satış': '24,1457'}, 
             'İsveç Kronu': {'alış': '3,0906', 'satış': '3,1061'}, 
             'Ruble': {'alış': '0,3751', 'satış': '0,3770'}}
             } 
class Currency():
    def getCurrency():
        url = "https://bigpara.hurriyet.com.tr/doviz/dolar/"
        driver = webdriver.Chrome()
        driver.get(url)


        response = requests.get(url=url)
        soup = BeautifulSoup(response.content, "html.parser")
        # Para birimlerini ve değerlerini al
        for ul in soup.find_all('ul', {'style': 'background: rgb(255, 255, 255);'}):
            name = ul.find('h3').get_text(strip=True)
            values = ul.find_all('li', class_='cell015')
            buy_value = values[0].get_text(strip=True)
            sell_value = values[1].get_text(strip=True)
            my_dict['timestamp'] = time.time()

            my_dict['data'][name] = {
                "alış": buy_value,
                "satış": sell_value
            }
            print(f"{name}: Satış - {sell_value}, Alış - {buy_value}")

        driver.quit()


def update_currency():
    try:
        Currency.getCurrency()
        date_label.config(text="Güncellenme Tarihi: " + convert_to_datetime(my_dict['timestamp']))
    except:
        print("data could not be retrieved successfully")

    status_label.config(text="Döviz bilgileri güncellendi")

def convert_currency():
    selected_currency = currencychoosen.get()
    if not amount_entry.get().isdigit():  # Kullanıcı girdisi sayısal değilse
        messagebox.showerror("Geçersiz Girdi", "Lütfen miktara sayısal bir değer giriniz.")
    else:
        amount = float(amount_entry.get())
        if selected_currency in my_dict['data']:
            buy_rate = float(my_dict['data'][selected_currency]["alış"].replace(",", "."))
            converted_amount = amount * buy_rate
            result_label.config(text=f"{amount} {selected_currency} = {converted_amount:.2f} TRY")
        else:
            result_label.config(text="Geçersiz döviz")


# Tkinter window setup
window = tk.Tk()
window.title("Currency Converter")
window.geometry("450x500")

tk.Label(window, text="Döviz Dönüştürücü", font="Verdana 12").pack(pady=10)

  
# label 
ttk.Label(window, text = "Para Birimi Seçiniz:", 
          font = ("Verdana", 12)).pack(padx=10,pady=15)
  
# Combobox creation 
n = tk.StringVar() 
currencychoosen = ttk.Combobox(window, width = 27, textvariable = n) 
  
# Adding combobox drop down list 
currencychoosen['values'] = list(my_dict['data'].keys())

currencychoosen.pack(pady=5)


tk.Label(window, text="Miktar Giriniz:", font="Verdana 12").pack(pady=10)
amount_entry = tk.Entry(window, font="Verdana 12")
amount_entry.pack(pady=5)

convert_button = tk.Button(window, text="Dönüştür", font="Verdana 12",command=convert_currency)
convert_button.pack(pady=5)

result_label = tk.Label(window, text="", font="Verdana 12")
result_label.pack(pady=5)

def convert_to_datetime(timestamp:int) -> str:
    dt_object = datetime.fromtimestamp(my_dict['timestamp'])
    date_time = dt_object.strftime('%Y-%m-%d %H:%M')
    return date_time



date_label = tk.Label(window, text="En son güncelleme: " + convert_to_datetime(my_dict['timestamp']), font="Verdana 12")
date_label.pack(pady=5)


update_button = tk.Button(window, text="Döviz verilerini güncelle", font="Verdana 12", command=update_currency)
update_button.pack(pady=5)

status_label = tk.Label(window, text="", font="Verdana 12")
status_label.pack(pady=5)

window.mainloop()


