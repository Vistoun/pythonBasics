'''
Tuples - neměnitelné n-tice hodnot (seřazený seznam prvků)
In Python tuples are written with round brackets.
V Pythou se tuples zapisují s kulatými závorky 
'''

# Vytvoření tuples
numbers = (1, 2, 3)
print('numbers: ', numbers)
print('Type(numbers): ',type(numbers))

chars = tuple('Hello world')
print('chars: ', chars)
print('Type(chars): ',type(chars))

# To create a tuple with only one item, you have add a comma after the item, unless Python will not recognize the variable as a tuple.
# pro vytvoření tuplu s jednou položkou, musíte přidat čárku za položku
colors = ('red',)
print('colors: ', colors)

# Součet tuples
print(f'chars + numbers: {chars + numbers}')

# Výpis hodnot 
# You can specify a range of indexes by specifying where to start and where to end the range.
# můžete specifokovat rozsah indexu tím, že specifikujeme kde začit a kde skončí rozsah
# When specifying a range, the return value will be a new tuple with the specified items.
# Když se specifukuje rozsah, vracená hodnota bude nový tuple se specifokovanýmy itemy
print(f'chars[2:5]: {chars[2:5]}')

# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
# negativní indexování znamená začatek od konce, -1 odkazuje na poslední položku, -2 odkatuje na druhou psolední položku a tak dále
# Specify negative indexes if you want to start the search from the end of the tuple: 
# Spefikuj zaporný index pokud chcete začínat hledat od konce tuplu  
# This example returns the items from index -4 (included) to index -1 (excluded)
# tento příklad vrací položku z indexu -4 (zahrnuta) do indexu -1  
print(f'chars[-4:-1]: {chars[-4:-1]}')

# To determine how many items a tuple has, use the len() method:
# Pro určení kolik položek má tuple, použijte metodu len()
print(f'len(chars): {len(chars)}')

# Zjištění prvního výskytu a počtu výskytu prvku
if 'l' in chars:
    print(f'chars.index("l"): {chars.index("l")}')
    print(f'chars.count("l"): {chars.count("l")}')

# Záměna hodnot proměnných
x = 10
y = 2
x, y = y, x
print(f'x: {x}, y: {y}')
