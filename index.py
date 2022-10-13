from datetime import date

today = date.today()
time = today.timetuple()
y, m, d, h, min, sec, wd, yd, i = time
if(h < 18 & h > 12) :
    print("Bonjour ! ")
if(h < 12) : 
    print("Have a good day !")
else :
    print('добрый вечер !') # Bonsoir en russe 
word = input("Donnez un mot !")
if(word == word[::-1]):
    print('Bien joué !')
else : 
    print('Dommage !')