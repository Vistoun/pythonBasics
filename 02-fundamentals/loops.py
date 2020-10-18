''' Příklady cyklů v Pythonu '''
# Cykly for
for number in range(1, 10, 2):
    print("Cislo ", number, number * ".")

# Součástí cyklu for může být část else
successful = False
for number in range(3):
    print("Pokus ", number)
    if successful:
        print("Uspesne spojeni")
        break
else:
    print("Spojeni se nezdarilo")

# Vnořené cykly
for x in range(5):
    for y in range(2, 4):
        print(f"({x} na {y}) = {x ** y}")

# Hodnoty, které je možné iterovat
for char in "Opakovani":
    print(f"{char} = {ord(char)}")

for num in [1, 8, 12, 47]:
    print(f"{num} = {'sude' if num % 2 == 0 else 'liche'}")

# Cykly while
# Převod desítkového čísla na binární
dec = 56
bin = ""
while dec != 0:
    bin = str(dec % 2) + bin
    dec //= 2
print(f"Binarni cislo = {bin}")

# Smyčka pro ukončení programu zadáním příkazu q (quit)
command = ""
while command.lower() != "q":
    command = input(">")
    print("Ukonci program zadanim pismene \"q\"")
print("Program ukoncen")

while True:
    print("Ukonci program zadanim pismene \"q\"")
    command = input(">")
    if command.lower() == "q":
        break
print("Program ukoncen")
