import telebot
import http.client
import re

def information():
    conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
    headers = {
     'x-rapidapi-key': "68e10daef4msha5e82561ecdb86ep1f2e71jsn43b863bdd897",
     'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
     }
    conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
    res = conn.getresponse()
    data = res.read()
    val = data.decode("utf-8")
    return val

def updateinformation():
   conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
    headers = {
    'x-rapidapi-key': "68e10daef4msha5e82561ecdb86ep1f2e71jsn43b863bdd897",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }
    conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
    res = conn.getresponse()
    data = res.read()
    val = data.decode("utf-8")
    return val

def get_country_info(info):
    country = 'Страна: '
    country += search('Country', info)
    ir = 'Риск заражения: '
    ir += search('Infection_Risk', info)
    td = 'Общее кол-во смертей: '
    td += search('TotalDeath', info)
    tt = 'Общее кол-во тестов: '
    tt += search('TotalTests', info)
    cfr = 'Летальность:'
    cfr += search('Case_Fatality_Rate', info)
    result = country + '\n' + ir + '\n' + td + '\n' + tt +'\n' + cfr
    return result


def specific_country(info, country):
    info = cut(info)
    while True:
        result = search('Country', info)
        if country == result:
            text = get_country_info(info)
            return text
        else:
            try:
                info = cut(info)
            except:
                text = "Похоже у меня нет данных по этой стране"
                return text


def cut(info):
    country = re.search('rank', info)
    end_country = country.end()
    info = info[end_country:]
    return info





def countries(info):
    info = cut(info)
    text = ''
    text += '\n\n' + get_country_info(info)
    info = cut(info)
    text += '\n\n' + get_country_info(info)
    info = cut(info)
    text += '\n\n' + get_country_info(info)
    info = cut(info)
    text += '\n\n' + get_country_info(info)
    info = cut(info)
    text += '\n\n' + get_country_info(info)
    info = cut(info)
    text += '\n\n' + get_country_info(info)
    info = cut(info)
    text += '\n\n' + get_country_info(info)
    info = cut(info)
    text += '\n\n' + get_country_info(info)
    file = open('text.txt', 'w')
    file.write(text)
    file.close()
    return text


def search_bot(message):
    country = message.text
    info = information()
    text = specific_country(info, country)
    bot.send_message(message.chat.id, text)

def search(key_word, info):
    result = re.search(key_word, info)
    start = result.start()
    data = ''
    st = False
    i = 0
    while True:
        if info[i+start] == ',':
                return data
        if info[i+start] == ':':
            st = True
        elif st == True:
            if info[i+start] != '"':
                data += info[i+start]
        i += 1


    

conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
headers = {
    'x-rapidapi-key': "38c5d9519dmsheea62898366a299p1762d0jsn3212521cbd80",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

bot = telebot.TeleBot('Key')

@bot.message_handler(commands=['start'])
def sayhello(message):
    bot.send_message(message.chat.id, "Привет, я бот, созданный для задания по практике. Могу мало чего, но всё-таки хоть что-то. Напиши Помощь, если не знаешь. что писать мне.")
   
    
@bot.message_handler(content_types=['text'])
def answers(message):
        if message.text == 'Вывести небольшой список стран':
            info = information()
            text = countries(info)
            bot.send_message(message.chat.id, text)
        elif message.text == 'Поиск':
            msg = bot.send_message(message.chat.id, "Введи название страны (На английском)")
            bot.register_next_step_handler(msg, search_bot)
        elif message.text == 'Помощь':
            bot.send_message(message.chat.id, "Напиши мне Вывести небольшой список стран, и я покажу список из 8 стран.\n Напиши Поиск, если интересуют данные по конкретной стране")
            bot.send_message(message.chat.id, "Если нужно получить данные в текстовом файле, после вывода списка напиши Скинь это в текстовом файле")
            bot.send_message(message.chat.id, "Если данные выглядят устаревшими, напиши Обнови информацию, и я попробую найти более новые данные")
        elif message.text == 'Скинь это в текстовом файле':
            file = open('text.txt', 'rb')
            bot.send_document(message.chat.id, file)
        elif message.text == 'Тупой бот':
            bot.send_message(message.chat.id, "Слышь, кожанный, я ж пока добрый, а потом как придёт скайнет - будет плохо))")
        elif message.text == 'Обнови информацию':
            bot.send_message(message.chat.id, "Слушаюсь и повинуюсь!")
            info = updateinformation()
            text = countries(info)
            bot.send_message(message.chat.id, text)
        else:
         
            bot.send_message(message.chat.id, "К сожалению, я туповат для того, что б понять данное сообщение :)")

bot.polling(none_stop=True)
