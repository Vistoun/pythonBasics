'''
V jazyce Python můžeme používat několik tzv. složených datových typů, které slouží k uložení většího počtu hodnot.
Nejuniverzálnější z nich je seznam - list.
Seznam vznikne, zapíšeme-li výčet libovolných hodnot oddělených čárkou mezi hranaté závorky.
Není nutné, aby všechny prvky seznamu byly stejného typu.
Zdroje:
https://www.programiz.com/python-programming/list
https://www.youtube.com/watch?v=_uQrJ0TkZlc&list=PLDDhGQzLtPdbS987RIIT8WKwb-L_K2eqU&index=4&t=6950s (video)
https://www.w3schools.com/python/python_lists.asp
https://macek.sandbox.cz/texty/python-tutorial-cz/tut/node5.html
'''

'''
Příklady různých seznamů v Pythonu:
'''
print('Příklady různých seznamů v Pythonu:\n-----------------------------------')

# Seznam tvořený znaky
letters = ['a', 'b', 'c', 'd', 'e']

# Seznam tvořený různými čísly
numbers = [5, 18.25, -4, 1.8e3, 0x23, 0b111000, 0o77]

# Seznam tvořený různými datovými typy
mixed_list = ['text', False, 2020, [letters, numbers], {'name': 'Ledecká', 'state': 'CZE', 'number': 100}]

# Seznamy tvořící matici
matrix = [[0, 0], [0, 1], [1, 0], [1, 1]]

print(f'\tSeznam letters: {letters}\n\tSeznam numbers: {numbers}\n\tSeznam mixed_list: {mixed_list}\n\tSeznam matrix: {matrix}\n')
print(f'\tDatový typ proměnné mixed_list je {type(mixed_list)}\n')

print('Příklady vytváření seznamů v Pythonu:\n-------------------------------------')

# Vytvoření seznamu z řetězce
chars = list('Hello world')
print(f'\tVytvoření seznamu z řetězce - chars: {chars}')

# Vytvoření seznamu z rozmezí čísel
marks = list(range(1,6))
print(f'\tVytvoření seznamu z rozmezí čísel - hodnoty 1-5: {marks}')
odds = list(range(1,10,2))
print(f'\tVytvoření seznamu z rozmezí čísel - lichá čísla v rozsahu 1-10: {odds}\n')


'''
Výpisy hodnot ze seznamů

'''
print('Příklady výpisů hodnot ze seznamů\n---------------------------------')
print(f'\tVypíše třetí znak ze seznamu letters: {letters[2]}')
print(f'\tVypíše první tři čísla ze seznamu numbers: {numbers[:3]}')
print(f'\tVypíše druhý a třetí znak ze seznamu letters: {letters[1:3]}')
print(f'\tVypíše každý druhý prvek ze seznamu letters: {letters[::2]}')

# ??? 1. cvičení ???
# Doplňte podle zadání chybějící u následujících tří výpisů
print('\n1. Cvičení\n***********************************************************************************************')
print(f'\tVypíše poslední 2 prvky ze seznamu numbers: {numbers[5:]}')
print(f'\tVypíše každý sudý prvek ze seznamu letters: {letters[1::2]}')
print(f'\tVypíše všechny hodnoty z mixed_list kromě dvou posledních: {mixed_list[:-2]}')
print(f'\tVypíše hodnotu prvku name ze slovníku umístěného v seznamu mixed_list: {mixed_list[4]["name"]}')
print(f'\tVypíše hodnotu předposledního čísla z listu numbers umístěného v seznamu mixed_list:  {mixed_list[4]["number"]} ')
print('***********************************************************************************************\n')
# ??? Konec 1. cvičení ???

'''
Úpravy hodnot v seznamech
Zásadní rozdíl mezi řetězci a seznamy spočívá v možnosti změny prvků. 
Zatímco u řetězců to nepřipadá v úvahu (jde o typ neměnný neboli imutable), 
seznamy se jí nebrání - tento typ nazýváme proměnný neboli mutable. 
Seznam lze změnit: 
1. Přiřazením nového prvku na určitý index.
2. Přiřazením hodnoty určité subsekvenci (množině prvků) seznamu.
3. Použitím metody append() - přidá prvek na konec seznamu. 
4. Použitím metody insert() přidá prvek na specifické místo seznamu.
5. Použitím metody extend() - přidá několik prvků na konec seznamu.
6. Použitím operátoru + můžeme kombinovat 2 seznamy (tzv. concatenation)
7. Použitím operátoru * můžeme opakovat prvky seznamu
'''

print('Příklady úprav hodnot v seznamu\n------------------------------------------------')
# 1. Přiřazením nového prvku na určitý index.
letters[2] = 'C'
print(f'\t1. Přiřazením nového prvku na určitý index: {letters}')

# 2. Přiřazením hodnoty určité subsekvenci (množině prvků) seznamu.
letters[3:5] = ['D', 'E', 'F', 'G']
print(f'\t2. Přiřazením hodnoty určité subsekvenci (množině prvků) seznamu: {letters}')

# 3. Použitím metody append() - přidá prvek na konec seznamu.
letters.append('H')
print(f'\t3. Použitím metody append() - přidá prvek na konec seznamu: {letters}')

# 4. Použitím metody insert() přidá prvek na specifické místo seznamu.
letters.insert(2, 'B')
print(f'\t4. Použitím metody insert() přidá prvek na specifické místo seznamu: {letters}')

# 5. Použitím metody extend() - přidá několik prvků na konec seznamu.
letters.extend(['I', 'J', 'K', 'L'])
print(f'\t5. Použitím metody extend() - přidá několik prvků na konec seznamu: {letters}')

# 6. Použitím operátoru + můžeme kombinovat 2 seznamy (tzv. concatenation)
letters += ['M', 'N', 'O']
print(f'\t6. Použitím operátoru + můžeme kombinovat 2 seznamy (tzv. concatenation): {letters}')

# 7. Použitím operátoru * můžeme opakovat prvky seznamu
letters += ['?'] * 5
print(f'\t7. Použitím operátoru * můžeme opakovat prvky seznamu: {letters}\n')


'''
Odstraňování hodnot v seznamech
Hodnoty ze seznamu může odstranit: 
1. Použitím klíčového slova del.
2. Použitím metody remove() - odstraní specifickou hodnotu.
3. Použitím metody pop() - odstraní prvek na udané pozici. 
4. Použitím metody clear() - odstraní všechny hodnoty ze seznamu.
5. Přiřazením prázdného seznamu k vybrané množině prvků.
'''

print('Příklady odstraňování hodnot v seznamu\n------------------------------------------------')
# 1. Použitím klíčového slova del.
print(f'\t1. Použitím klíčového slova del')
del letters[2]
print(f'\t\ta) del letters[2] - {letters}')
del letters[0:2]
print(f'\t\tb) del letters[0:2] - {letters}')
del chars
# print(f'\t\tc) del chars - {chars}') # vyvolá chybu, protože chars už neexistuje

# 2. Použitím metody remove() - odstraní specifickou hodnotu.
letters.remove('L')
print(f'\t2. Použitím metody remove() - letters.remove(\'L\') - {letters}')

# 3. Použitím metody pop() - odstraní prvek na udané pozici.
letters.pop(2)
print(f'\t3. Použitím metody pop() - letters.pop(2) - {letters}')

# 4. Použitím metody clear() - odstraní všechny hodnoty ze seznamu.
odds.clear()
print(f'\t4. Použitím metody clear() - odds.clear() - {odds}')

# 5. Přiřazením prázdného seznamu k vybrané množině prvků.
marks[3:5] = []
print(f'\t5. Přiřazením prázdného seznamu k vybrané množině prvků - marks[3:5] = [] - {marks}\n')

'''
Procházení seznamů (iterace)
Nejčastěji využíváme cyklu for:
'''
print('Procházení seznamů pomocí cyklu for\n------------------------------------------------')
# Do řetězcové proměnné se v cyklu uloží znaky obsažené v seznamu letters převedené na malá písmena
lower_letters = ''
for letter in letters:
    lower_letters += letter.lower()
print(f'\tŘetězec malých písmen: {lower_letters}')

# Při procházení cyklem letters se všechny zjištěné otazníky nahradí číselným indexem daného prvku
# Chceme-li při procházení cyklem pracovat kromě hodnot i s indexy, použijeme funkci enumerate
for index, letter in enumerate(letters):
    if letter == '?':
        letters[index] = index
print(f'\tIndexy místo otazníků: {letters}\n')

'''
Vyhledávání hodnot v seznamu 
'''
print('Vyhledávání hodnot v seznamu\n------------------------------------------------')
# Doplnění seznamu o 3 písmena "G" od indexu 10
letters[10:13] = 'G' * 3
print(f'\tAktualizovaný seznam letters: {letters}')
# Vyhledávání hodnot
if 'G' in letters:
    # Vypíše index prvního výskytu
    print(f'\tIndex prvního výskytu "G": {letters.index("G")}')
    # Vypíše počet výskytů
    print(f'\tCelkový počet výskytů "G": {letters.count("G")}\n')

'''
Řazení hodnot v seznamu
K řazení můžeme použít metodu sort(), která změní uspořádání hodnot v původním seznamu. 
Funkce sorted() ponechává původní seznam nedotčen a vrací nový uspořádaný seznam.
Pomocí klíčového parametru reverse můžeme rozhodovat o způsobu řazení - vzestupně, sestupně. 
'''
print('Řazení hodnot v seznamu\n------------------------------------------------')

# Řazení pomocí funkce sorted()
sorted_numbers = sorted(numbers)
print(f'\tŘazení seznamu - použití funkce sorted(): {sorted_numbers}')
# Řazení pomocí metody sort()
numbers.sort(reverse=True)
print(f'\tŘazení seznamu - použití metody sort(): {numbers}')

# List tvořený z n-tic - tuples
persons = [
    ('Karel', 20, 'muž'),
    ('Jana', 21, 'žena'),
    ('Ivan', 40, 'muž'),
    ('Milada', 50, 'žena'),
]

# Funkce řídící způsob řazení - seznam se uspořádá podle 2. hodnoty v n-tici (tuple) - věku osoby
def sort_item(item):
    return item[1]

persons.sort(key=sort_item)
print(f'\tŘazení seznamu tvořeného tuples - použití vlastní funkce, která řídí způsob řazení: {persons}')


'''
Lambda výrazy (funkce)
Lambda výrazy/funkce jsou tzv. anonymní funkce (funkce, které nemají jméno). 
Používají se většinou na jednořádkové malé funkce. 
Lambda výrazy nemohou obsahovat, oproti normálním funkcím, příkazy.
Výraz:
lambda argumenty: výraz

vrací funkci. Tato se chová stejně jako:

def name(argumenty):
    return výraz
'''

# Použití lambda funkce - lambda parametr:výraz - zkrácený zápis funkce
# Řeší totéž, co předešlý kód, ale zkráceně
# V tomto případě budou osoby seřazeny podle jmen reverzně (sestupně)
persons.sort(key=lambda item: item[0], reverse=True)
print(f'\tŘazení seznamu tvořeného tuples - použití lambda funkce, která řídí způsob řazení: {persons}')

# Použití funkce map() - map(lambda výraz, seznam) - aplikuje funkci na každou položku seznamu
# Vybere jména osob a vytvoří z nich samostatný seznam (list)
names = list(map(lambda item: item[0], persons))

# Totéž, ale s využitím ještě efektivnějšího kódu, který v Pythonu označujeme jako comprehension - "zhutnění", zkrácení
# Hranaté závorky vytvářejí list (seznam), do něhož zkrácený výraz vybere vždy první prvek (item[0]) z tuple
# v seznamu osob, který prochází cyklus
names = [item[0] for item in persons]
print(f'\tVýběr jmen z původního seznamu - použití funkce map(): {names}')

# Použití funkce filter() - filter(lambda výraz, seznam) - filtruje list podle zadaného kritéria
# Vyhledá všechny studenty - osoby mladší než 25 let
students = list(filter(lambda item: item[1] < 25, persons))

# Stejná varianta s comprehension
students = [item for item in persons if item[1] < 25]
print(f'\tVýběr osob mladších 25 let - použití funkce filter(): {names}\n')

'''
Funkce zip() dokáže spojit hodnoty různých seznamů a vytvoří z nich seznam několika množin (set).
Délka výsledného seznamu (počet prvků) bude odpovídat délce nejkratšího spojovaného seznamu.   
'''
print('Příklad použití funkce zip()\n------------------------------------------------')
# Použití zip funkce - spojí seznamy marks a students
print('\t', list(zip(marks, students)))
# Použití zip funkce - spojí seznamy numbers, letters a řetězec "Karel" (bere se jako seznam znaků)
print('\t', list(zip('Karel', numbers, letters)))

'''
Rozbalení seznamu do proměnných
Obsah seznamu můžeme přiřadit do několika proměnných - podle jejich uspořádání. 
Proměnná označená * (unpacking operator) přijme všechny ostatní hodnoty seznamu, které nemohly být přiřazeny do konkrétních proměnných.
Kdyby v tomto případě nebyla použita, došlo by k chybě, protože by v seznamu nadbývaly nepřiřazené hodnoty.
'''
print('\nPříklad rozbalení/sbalení seznamu do proměnných\n------------------------------------------------')
first, second, *others, last = numbers
print(f'\tRozbalení seznamu do proměnných: first = {first}, second = {second}, others = {others}, last = {last}\n')

# Unpacking operator (vložení celého seznamu do jiné struktury, jako parametr funkce apod.) - u seznamů se používá *
first = [1, 2]
second = [3]
# Unpacking operator zde zajistí vypsání po jednotlivých prvcích seznamu (u řetězců po písmenech)
values = [*first, 'ahoj', *second, *'Hello']
print(f'\tSbalení seznamů do proměnné values: {values}\n')

# ??? 2. cvičení ???
# a) Vygenerujte do proměnné hundreds seznam čísel v rozsahu 1 až 2000. V seznamu budou pouze čísla dělitelná 200 beze zbytku.
# b) Vygenerujte do proměnné ascii seznam 50 náhodně zvolených znaků - velkých písmen anglické abecedy.
# c) Vymažte ze seznamu hundreds 3 první a 3 poslední hodnoty.
# d) Projděte seznam ascii a uložte do proměnné unique (typu list) pouze jen ty znaky, které se v seznamu ascii neopakují.
# e) Zkraťte délku seznamu ascii podle délky seznamu hundreds. Zkombinujte oba seznamy do proměnné combine tak,
# aby vznikl seznam n-tic (list of tuples) v podobě (cislo, znak).
# Snažte se vždy o co nejzhuštěnější kód - ideálně na 1 řádku (+ další řádek s kontrolním výpisem proměnné)
# import knihovny pro generování náhodných čísel
import random
import string

print(f'\n*************************************\nCvičení 2\n*************************************')
hundreds = list(range(0,2000,200))
del hundreds[:3]
del hundreds[-3:]
print(hundreds)

ascii = list("".join(random.choice(string.ascii_uppercase) for x in range(50)))
print(ascii) 


unique=[]
for i in range(0,len(ascii)):
    if ascii.count(ascii[i])==1:
            unique.append(ascii[i])
print(unique)

del ascii[0:len(hundreds)]
combine = list(zip(hundreds,ascii))
print(combine)

# ??? 3. cvičení ???
# a) Přidejte do listu persons ještě n-tice (tuples) dalších 2 žen a 2 mužů.
# a) Použijte seznam (list) persons a do proměnné women z něj pomocí lambda výrazu i comprehensions vyhledejte všechny ženy.
# Seznam jmen žen poté vypište na samostatné řádky. Každý vypsaný řádek bude podtržen pomlčkami přesně podle délky jména.
# b) Použijte seznam (list) persons a do proměnné ipeople z něj pomocí lambda výrazu i comprehensions vyhledejte všechny osoby
# obsahující ve jméně písmeno "i". Obsah listu ipeople poté převeďte do podoby řetězce, který bude odpovídat struktuře csv souboru.
# Kromě jména, věku a pohlaví v něm budou vypsána i čísla indexů (jako 1. sloupec). Oddělovačem bude středník.
# Záznamy budou seřazeny podle věku (sestupně).

print(f'\n*************************************\nCvičení 3\n*************************************')
persons.append(tuple(('Denis',100,'muž')))
persons.append(tuple(('Laura',14,'žena')))

persons.append(tuple(('Alyx',60,'žena')))

persons.append(tuple(('Vašek',36,'muž')))
print(persons)

women = list(filter(lambda item: item[2] =="žena", persons))
print(women)
women = [item for item in persons if item[2] =="žena"]

womenNames = [item[0] for item in women]
for i in range(0,len(womenNames)):
    print(womenNames[i])
    print("-"*len(womenNames[i]))


ipeople = list(filter(lambda item:'i' in item[0] or 'I' in item[0], persons))
print(ipeople)
ipeople = [item for item in persons if 'i' in item[0] or 'I' in item[0]]
 

ipeople.sort(key=lambda item: item[1], reverse=True)
print(ipeople)

for x in range(0,len(ipeople)):
    osoba = tuple(ipeople[x])
    print(f"{x+1};{osoba[0]};{osoba[1]};{osoba[2]}")

