moje_zadania = []

while True:
    wybor = input("Co chcesz zrobić? (1-dodaj, 2-pokaz, 3-koniec, 4-usun): ")
    if wybor == "1":
        zadanie = input("Jakie zadanie chcesz dodac: ")
        moje_zadania.append(zadanie)
        print(f"{zadanie} dodane! Co dalej?")
    elif wybor == "2":
        for z in enumerate(moje_zadania, start=1): print(z)
        print(f"Twoje zadania: {moje_zadania}")
    elif wybor == "3":
        print("Do widzenia!")
        break
    elif wybor == "4":
        wybor_2 = input("Usun pierwszy element (1), lub usun po nazwie (2)")
        if wybor_2 == "1":
            print(f"Lista {moje_zadania}")
            for zadanie in moje_zadania.pop(0):
                print("Usunieto pierwsza pozycje")
        elif wybor_2 == "2":
            moje_zadania.remove(input("Wprowadz nazwe pozycji do usuniecia: "))
            print("Usunieto!")
    else:
        print("niepoprawny wybor")






