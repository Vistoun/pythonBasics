'''
Odsazování v Pythonu (indentation)

Většina programovacích jazyků jako C, C++, Java nebo JavaScript používá k vymezení bloků kódu složené závorky (braces).
V Pythonu se používá odsazování. Blok kódu (např. tělo funkce, cyklu atd.) tedy začíná s odsazením a končí prvním
neodsazeným řádkem.
Počet mezer v odsazení je libovolný, ale musí být konzistentní aspoň v rámci jednoho bloku.
K odsazení musí být použita minimálně jedna mezera.
Obvykle se k odsazování používá tubulátor, který bývá nejčastěji nastaven na 4 mezery.
'''

# Odsazení bloku kódu uvnitř cyklu a podmínky
for i in range(1, 10):
    print(i)
    if i % 2 == 0:
        print('even')
    else:
        print('odd')


'''
Dokumentační řetězce v Pythonu (docstrings)

Víceřádkový řetězec následující hned po záhlaví funkce v Pythonu je nazýván docstring (documentation string neboli 
dokumentační řetězec) a obsahuje stručné vysvětlení toho, co funkce provádí.
Přestože je to nepovinný doplněk programového kódu, je považován za "good programming practice", tedy jednu z dobrých
zásad, které by měl programátor v Pythonu dodržovat.
Docstrings se zapisují mezi trojnásobné uvozovky (tedy podobně jako komentáře).
Tyto dokumentační řetězce jsou přístupné prostřednictvím "magického" __doc__ atributu funkce.    
'''

# Odsazení bloku kódu uvnitř funkce a použití docstring
def greet(name):
    """
    This function greets to the person
    passed in as a parameter
    """
    print("Ahoj, " + name + "!")

# Vypíše docstring spojený s funkcí greet
print(greet.__doc__)
# Vyvolá funkci greet s parametrem 'Hilda'
greet('Hilda')

"""
Cvičení 2:

Vytvořte libovolně pojmenovanou vlastní funkci s minimálně jedním parametrem, v níž využijete cyklus for, 
aspoň jednu podmínku if a funkci print(). Dodržte správné odsazování kódu a opatřete funkci stručnou dokumentací.
Do konzole vypište nejprve docstring vaší funkce a potom zavolejte funkci samotnou.   
"""

def test(number):
    """
    V této se dopočíta čislo, ktere je zadané jako parametr funkce, je-li vetší než 0
    """
    if(number > 0):
        for i in range(number):
            print(i)
            
print(test.__doc__)
test(8)

