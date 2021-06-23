import http.client
from tkinter import *
import tkinter as tk
import re
import sys




#Получение информации с сервера:
conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "a0580e8b98mshde852a61dc71befp1f85d5jsne85be2246ec5",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
   }

conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
res = conn.getresponse()
data = res.read()
val = data.decode("utf-8")

win = tk.Tk()
win.geometry(f"740x440+100+200")
win.title("Task#3")

#Функция для обновления информации:
def update():
    conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")

    headers = {
    'x-rapidapi-key': "a0580e8b98mshde852a61dc71befp1f85d5jsne85be2246ec5",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
   }

    conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
    res = conn.getresponse()
    data = res.read()
    val = data.decode("utf-8")
    print(val)

#Функции, которые будут искать необходимые значения(Каждая из них берёт отрезок между num1 u num2, потому что в этих рамках находяться
#наши значения.
def Infection_Risk(country):
        num = val.find('Infection_Risk',val.find(country))
        num2 = val.find('Case_Fatality_Rate',val.find(country))
        return val[num+16:num2-2]

def Case_Fatality_Rate(country):
        num = val.find('Case_Fatality_Rate',val.find(country))
        num2 = val.find('Test_Percentage',val.find(country))
        return val[num+20:num2-2]

def Total_Deaths(country):
        num = val.find('TotalDeaths',val.find(country))
        num2 = val.find('NewDeaths',val.find(country))
        return val[num+13:num2-2]

def Total_Tests(country):
        num = val.find('TotalTests',val.find(country))
        num2 = val.find('Population',val.find(country))
        return val[num+13:num2-3]

def Population(country):
        num = val.find('Population',val.find(country))
        num2 = val.find('one_Caseevery_X_ppl',val.find(country))
        return val[num+13:num2-3]


def label(text):
    return Label(win, text=text,font=('Arial', 13), height=2)

# Вывод информации
label(Infection_Risk('Hungary')).grid(column=1, row=1)
label(Infection_Risk('Russia')).grid(column=1, row=2)
label(Infection_Risk('UK')).grid(column=1, row=3)
label(Infection_Risk('Ukraine')).grid(column=1, row=4)
label(Infection_Risk('Netherlands')).grid(column=1, row=5)
label(Case_Fatality_Rate('Hungary')).grid(column=2, row=1)
label(Case_Fatality_Rate('Russia')).grid(column=2, row=2)
label(Case_Fatality_Rate('UK')).grid(column=2, row=3)
label(Case_Fatality_Rate('Ukraine')).grid(column=2, row=4)
label(Case_Fatality_Rate('Netherlands')).grid(column=2, row=5)
label(Total_Deaths('Hungary')).grid(column=3, row=1)
label(Total_Deaths('Russia')).grid(column=3, row=2)
label(Total_Deaths('UK')).grid(column=3, row=3)
label(Total_Deaths('Ukraine')).grid(column=3, row=4)
label(Total_Deaths('Netherlands')).grid(column=3, row=5)
label(Total_Tests('Hungary')).grid(column=4, row=1)
label(Total_Tests('Russia')).grid(column=4, row=2)
label(Total_Tests('UK')).grid(column=4, row=3)
label(Total_Tests('Ukraine')).grid(column=4, row=4)
label(Total_Tests('Netherlands')).grid(column=4, row=5)
label(Population('Hungary')).grid(column=5, row=1)
label(Population('Russia')).grid(column=5, row=2)
label(Population('UK')).grid(column=5, row=3)
label(Population('Ukraine')).grid(column=5, row=4)
label(Population('Netherlands')).grid(column=5, row=5)

print(val)

#Кнопка и прочие елементы.

tk.Button(text='Update', bd=5,font=('Arial', 13), command=update).grid(row=6,column=6, stick='wens', padx=5, pady=5)


label("Country").grid(column=0, row=0)

label("Infection Risk").grid(column=1, row=0)

label("Case Fatality Rate").grid(column=2, row=0)

label("Total Deaths").grid(column=3, row=0)

label("Total Tests").grid(column=4, row=0)

label("Population").grid(column=5, row=0)

label('Hungary').grid(column=0, row=1)

label("Russia").grid(column=0, row=2)

label("UK").grid(column=0, row=3)

label("Ukraine").grid(column=0, row=4)

label("Netherlands").grid(column=0, row=5)

#Функция поиска по строке ввода. Крайне схожа с прошлыми, данные получаем аналогичным способом, только если страны нет - выводим No information
#  if (val.find(country)) == -1: данный рядок отвечает за проверку на отсутствие страны.

def get():
    conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")

    headers = {
    'x-rapidapi-key': "a0580e8b98mshde852a61dc71befp1f85d5jsne85be2246ec5",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
   }

    conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
    res = conn.getresponse()
    data = res.read()
    val = data.decode("utf-8")


    country = ent.get()

    if (val.find(country)) == -1:
        label('No information').grid(column=1, row=6)
    
        label('No information').grid(column=2, row=6)
    
        label('No information').grid(column=3, row=6)
 
        label('No information').grid(column=4, row=6)
    
        label('No information').grid(column=5, row=6)

        sys.exit()

# Данные  функции идентичны тем, что использовались для поиска ранее, только сейчас они сработают тогда, когда страна будет существовать в списке
    def Infection_Risk(country):
        num = val.find('Infection_Risk',val.find(country))
        num2 = val.find('Case_Fatality_Rate',val.find(country))
        return val[num+16:num2-2]

    def Case_Fatality_Rate(country):
        num = val.find('Case_Fatality_Rate',val.find(country))
        num2 = val.find('Test_Percentage',val.find(country))
        return val[num+20:num2-2]

    def Total_Deaths(country):
        num = val.find('TotalDeaths',val.find(country))
        num2 = val.find('NewDeaths',val.find(country))
        return val[num+13:num2-2]

    def Total_Tests(country):
        num = val.find('TotalTests',val.find(country))
        num2 = val.find('Population',val.find(country))
        return val[num+13:num2-3]

    def Population(country):
        num = val.find('Population',val.find(country))
        num2 = val.find('one_Caseevery_X_ppl',val.find(country))
        return val[num+13:num2-3]

#Аналогичный вывод, только уже с рядком страны, которую ввели в соответствующее поле.
    label(Infection_Risk(country)).grid(column=1, row=6)
    label(Case_Fatality_Rate(country)).grid(column=2, row=6)
    label(Total_Deaths(country)).grid(column=3, row=6)
    label(Total_Tests(country)).grid(column=4, row=6)
    label(Population(country)).grid(column=5, row=6)
    
#Создание поля и новой кнопки для получения информации по конкретной стране.
ent = tk.Entry(win, justify=tk.LEFT, font=('Arial', 13), width=2)
ent.insert(0, '')
ent.grid(row=6,column=0, stick='we', padx=5)


tk.Button(text='Get information about entered country', bd=5,font=('Arial', 13), command=get).place(x=10, y=320)

