biblioterka_filmow = []

while True:
    pozycja = input("Co chcesz zrobic? (1)Dodac film, (2)Pokaz i zakoncz: ")

    if pozycja == "1":
        moj_film = {}
        moj_film["tytul"] = input("Dodaj tytul: ")
        moj_film["rok"] = input("Dodaj rok: ")

        biblioterka_filmow.append(moj_film)
        for f in biblioterka_filmow:
            print(f"- {f['tytul']} ({f['rok']})")
    elif pozycja == "2":
        print("# BIBLIOTEKA #")
        for f in biblioterka_filmow:
            print(f"- {f['tytul']} ({f['rok']})")
        break
    else:
        print("Wybierz (1) lub (2)")



        
