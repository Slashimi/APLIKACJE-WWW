#zad1
a_list = [1, 2, 3, 4, 5]
b_list = [6, 7, 8 ,9, 10]
def funkcja(a_list, b_list):
    x = [i for i in a_list if i % 2 == 0]
    y = [i for i in b_list if i % 2 != 0]
    z = x + y
    return z
print(funkcja(a_list, b_list))

#zad2
data_text = "Dog"
def funkcja2(data_text):
    dict={
        'length': len(data_text),
        'letters': [char for char in data_text],
        'big_letters': data_text.upper(),
        'small_letters': data_text.lower(),
    }
    return dict
print(funkcja2(data_text))

#zad3
def funkcja3(text, letter):
    string = ""
    for char in text:
        if char != letter:
            string = string + char
    return string
print(funkcja3("ala ma kota", 'a'))

#zad4
def funkcja4(temp, temperature_type):
    if temperature_type == 'f':
        return (temp * 1.8) + 32
    elif temperature_type == 'k':
        return temp + 273.15
    elif temperature_type == 'r':
        return (temp * 1.8) + 491.67
    else:
        return "B��dny paametr!"
print(funkcja4(33, 'f'))

#zad5
class Calculator:
    def add(self):
        return "Dodaje"
    def difference(self):
        return "Odejmuje"
    def multiply(self):
        return "Mnoze"
    def divide(self):
        return "Dziele"

class ScienceCalculator(Calculator):
    def power(self):
        return "Poteguje"
    def element(self):
        return "Pierwiastkuje"

#zad6
def funkcja6(tekst):
    return tekst[::-1]
print(funkcja6("kote�"))