'''
Slovníky (dictionaries) podobně jako seznamy v sobě obsahují další hodnoty.
Na rozdíl od seznamů, ve kterých jsou všechny prvky uspořádané do jedné sekvence, ve slovnících máme dva druhy prvků:
klíč (angl. key) a hodnotu (angl. value).
Každému klíči je přiřazena jedna hodnota.
'''

# Collection which is unordered, changeable and indexed.
# kolekce která je nespořádná, změnitelná a indexovaná
# In Python dictionaries are written with curly brackets, and they have keys and values.
# v Pythonu slovniky se pišou ve složených zavorkách a maji kliče a hodnoty
car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}

point = {'x': 1, 'y': 10}

# Vytvoření slovníku pomocí konstruktoru dict()
point = dict(x=1, y=10)

# Změna hodnoty jednoho prvku slovníku
point['x'] = 2

# Vložení nového prvku do slovníku
point['z'] = 20

# Přístup k položkám slovníku
print(f'point["x"]: {point["x"]}')
print(f'point.get("x"): {point.get("x")}')

# Zjištění, zda existuje hodnota
if 'z' in point:
    print(f'point.get("z"): {point.get("z")}')

# Když hodnota neexistuje, vrací 0    
print(f'point.get("v", 0): {point.get("v", 0)}')

# Odstranění prvku ze slovníku  
del point['x']
print(f'point: {point}')

print(f'car.pop(): {car.pop("model")}')
00000000
# Odstraní poslední prvek ze slovníku
print(f'car.popitem(): {car.popitem()}')

# Procházení slovníkem - vypíše vždy pár klíč - hodnota
for key, value in point.items():
    print(f'{key} - {value}')

# Dictionary comprehension - zkráceně vytvoří slovník, jehož klíče tvoří čísla od 0 do 9 a hodnoty druhé mocniny 
values = {x: x ** 2 for x in range(10)}
print(f'values: {values}')

# Unpacking operator - pro slovníky se používají **
first = {'x': 1, 'y': 2}
second = {'x': 10, 'z': 5}
common = {**first, 'a': 15, **second}
print(f'common: {common}')

# Nested dictionary - vnořené slovníky
myfamily = {
  'child1' : {
    'name' : 'Emil',
    'year' : 2004
  },
  'child2' : {
    'name' : 'Tobias',
    'year' : 2007
  },
  'child3' : {
    'name' : 'Linus',
    'year' : 2011
  }
}
print(f'Nested dictionary myfamily: {myfamily}')

# ??? 4. cvičení ???
# a) Navrhněte vlastní vnořený slovník tvořený 3 reálnými objekty s aspoň 6 klíči tak, abyste kromě jednoduchých
# datových typů (čísla, řetězce, boolean) ve slovníku vhodně využili i všechny v tomto bloku probrané strukturované
# typy - tedy set, tuple a list.
# Volte příklad vycházející z reality - např. slovník aut, slovník filmů, slovník historických postav atd.
# b) Pomocí vhodných metod přidejte do slovníku nový prvek a nějaký starý naopak odstraňte
# c) Proveďte výpis obsahu slovníku tak, aby i v konzoli vytvořil hezky naformátovanou tabulku i s mezerami
# viz níže uvedený vzor.
'''
Slovník myfamily
---------------------------------------------
child           name                year
---------------------------------------------
child1          Emil                2004
child2          Tobias              2007
child3          Linus               2011
---------------------------------------------
Počet záznamů: 3
'''

mobiles = {
  "mobile1": {
    "model" : "iPhone 7",
    "year" :  2017,
    "storage": ["128GB", "64GB"],
    "nfc" : False,
    "colors" : {"Black", "Space Gray","Gray", "Red"},
    "network" : ("GSM", "LTE", "UMTS"),
    }, 
   "mobile2": {
    "model" : "iPhone XR",
    "year" :  2018,
    "storage": ["128GB", "64GB"],
    "nfc" : True,
    "colors" : {"Black", "Blue","Coral", "Red"},
    "network" : ("GSM", "LTE", "UMTS"),
  }, 
   "mobile3": {
    "model" : "Samsing Galaxy S20",
    "year" :  2020,
    "storage": ["128GB", "256GB"],
    "nfc" : True,
    "colors" : {"Green", "Levander","Navy Blue", "Orange", "Red", "White"},
    "network" : ("GSM", "LTE", "UMTS"),
  } 
}

del mobiles["mobile3"]

mobiles["mobile3"] = {
    "model" : "iPhone 8",
    "year" :  2018,
    "storage": ["128GB","256GB"],
    "nfc" : True,
    "colors" : {"Red", "Black","Space Gray", "White"},
    "network" : ("GSM", "LTE", "UMTS"),
}


print(" Model           Rok vydání     Uložiště                   NFC čip              Barvy                                        Podporované mobilní sítě")
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
print(" {mobile1[model]}        {mobile1[year]}           {mobile1[storage]}          {mobile1[nfc]}                {mobile1[colors]}       {mobile1[network]}".format(**mobiles))
print(" {mobile2[model]}       {mobile2[year]}           {mobile2[storage]}          {mobile2[nfc]}                 {mobile2[colors]}            {mobile2[network]}".format(**mobiles))
print(" {mobile3[model]}        {mobile3[year]}           {mobile3[storage]}         {mobile3[nfc]}                 {mobile3[colors]}      {mobile3[network]}".format(**mobiles))
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
