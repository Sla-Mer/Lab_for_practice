import re
rezultnumbers = []
string = input("Введіть рядок для опрацювання: ")

numbersarray = re.findall(r'\d+', string)
string = re.sub(r"\d+", "", string, flags=re.UNICODE)
numbersarray = [int(i) for i in numbersarray]
print("Рядок зі слів:\n", string, sep='')
print("Рядок з чисел, що були в початковому масиві:\n", numbersarray, sep='')

def cap(string):
    string, result = string.title(), ""
    for word in string.split():
        result += word[:-1] + word[-1].upper() + " "
    return result[:-1]
print("\nРядок слів після заміни першої та останньої літери на великі:\n", cap(string), sep='')
print("Максимальне число:",max(numbersarray))
max_index=numbersarray.index(max(numbersarray))
i=0
for i in range(len(numbersarray)):
    if i==max_index:
        continue
    temp = numbersarray[i] ** i
    rezultnumbers.append(temp)
print("Масив чисел, які піднесені до степеню по їх індексу(нумерація починається з 0, максимальне число не буде виведене):\n",rezultnumbers)
