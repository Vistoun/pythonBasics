# Operátory porovnávání
# == - zohledňuje logický typ
print(10 == "10")  # False
# Při porovnávání řetězců se vychází z hodnot kódů jednotlivých znaků
print("dad" > "bad")  # True
# Zjištění ordinální hodnoty kódu znaku
print(f"B={ord('B')}, b={ord('b')}")

# Podmínka v Pythonu
x = 1
if x > 0:
    print("Kladne")
elif x < 0:
    print("Zaporne")
else:
    print("Nula")

# Ternární operátor
age = 19
result = "dospely" if age >= 18 else "nedospely"
print(result)

# Logické operátory
year = 2016
print("lap year" if (year % 4 == 0 and year % 100 != 0)
      or year % 400 == 0 else "not lap year")

# Řetězení operátorů
if 18 <= age < 65:
    print("aktivni vek")
else:
    print("neaktivni vek")
