import http.client
from tkinter import *
import tkinter as tk
import re





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
win.geometry(f"640x340+100+200")
win.title("Task#3")

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

tk.Button(text='Update', bd=5,font=('Arial', 13), command=update).grid(row=6,column=5, stick='wens', padx=5, pady=5)


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

