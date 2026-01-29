# Program ma obliczyć ile każdy powinien zapłacić 
# przy podziale rachunku z uwzględnieniem napiwku.

rachunek = float(input("Ile wynosi rachunek? "))
napiwek = 10 # procent (np. 10%)
osoby = 4

# BŁĄD 1: Poniższa linijka wygeneruje TypeError. Dlaczego?
suma = rachunek * (1 + napiwek / 100)

# BŁĄD 2: Tutaj brakuje logicznego działania
na_osobe = float(suma) / int(osoby)

# BŁĄD 3: Program ma wypisać "Każdy płaci: [kwota]"
# Ale coś jest nie tak ze składnią printa poniżej
print(f"Każdy płaci:  {na_osobe}")

   