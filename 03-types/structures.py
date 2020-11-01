from collections import Counter 

string = "Tři sta třicet tři stříbrných stříkaček přestříkalo přes tři sta třicet tři stříbrných střech."

def charFrequency(string):
    chars = Counter(string).most_common()
    return list(chars)

print(charFrequency(string))