import time

print('FORMULARZ DANYCH')


while True: #Imie
    name = input('Podaj imie: ')
    
    if not name.isalpha(): #Sprawdzenie czy wprowadzono litery
        print('Imie nie moze zawierac liczb')
    elif name == "":
        print('Wypelnij puste pole')
    elif len(name) < 3:
        print('Imie jest zbyt krotkie')
    else:
        break

while True: #Nazwisko
    sec_name = input('Podaj nazwisko: ')
    
    if not sec_name.isalpha():
        print('Imie nie moze zawierac liczb')
    elif sec_name == "":
        print('Wypelnij puste pole')
    elif len(sec_name) < 3:
        print('Imie jest zbyt krotkie')
    elif name == sec_name:
        print('Nazwisko nie moze byc takie samo jak imie')
    else:
        break

while True: #Wiek
    age = input('Podaj wiek: ')
    
    if not age.isdigit(): #Sprawdzenie czy jest numerem
        if age == "":
            print('Wypelnij puste pole')
        else:
            print('Wiek nie moze zawierac liter')
    else:
        age = int(age)

        if age < 0:
            print('Wiek nie moze byc mniejszy niz 0')
        elif age >= 130:
            print('Wiek nie moze byc wiekszy niz 130')
        else:
            break

while True: #Miejscowosc
    city = input('Podaj miejscowosc: ')
    
    if not city.isalpha(): #Sprawdzenie czy wprowadzono litery
        print('Nazwa nie moze zawierac liczb')
    elif city == "":
        print('Wypelnij puste pole')
    elif len(city) < 3:
        print('Nazwa jest zbyt krotkia')
    else:
        break

while True: #Kod
    postal_code = input('Podaj kod pocztowy (bez spearatorow): ')
    
    if not postal_code.isdigit(): #Sprawdzenie czy jest numerem
        if postal_code == "":
            print('Wypelnij puste pole')
        else:
            print('Kod nie moze zawierac liter')
    else:
        postal_code = str(postal_code)
        if not len(postal_code) == 5: #Sprawdzenie dlugosci wprowadzonych znakow
            print('Kod musi zawierac 5 cyfr')
        else:
            break

while True: #Info o stanie danych
    data_accept = input('Czy pokazac wprowadzone dane? y/n: ').lower()

    if data_accept == "y":
        for t in range (10, 0, -1): # modul czasowy do odliczania zaimportowany na poczatku
            print(f'Ładowanie danych. Pozostało {t} s.')
            time.sleep(1)
        print(f'Imie: {name}, Nazwisko: {sec_name}, wiek: {age}, miejscowosc: {city}, kod pocztowy: {postal_code}')
        break
    elif data_accept == "n":
        print('Nie pokazuje danych')
        break
    else:
        print('Bledny wybor. Wpisz "y" lub "n".')
