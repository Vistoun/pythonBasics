'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.8 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.6 #? měsíční gravitace
SPEED_OF_LIGHT = 299792458  #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343  #? rychlost zvuku při teplotě 20 °C v suchém vzduchu


def gravityForce_earth(hmotnost):
    """
    Funkce pro výpočet gravitační síly na Zemi 
    """
    return format((hmotnost*EARTH_GRAVITY), ".2f")

def gravityForce_moon(hmotnost):
    """
    Funkce pro výpočet gravitační síly na Měsící 
    """
    
    return format((hmotnost*MOON_GRAVITY), ".2f")

def vypocetDrahy (cas):
    """
    Funkce pro výpočet dráhy za daný čas při rychlosti zvuku 
    """
    return(SPEED_OF_SOUND*cas)

def energie(hmotnost):
    """
    Funkce pro vypočet energie hmoty
    """
    return (hmotnost*(SPEED_OF_LIGHT**2))

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''

#vzdalení měsíce od Zěmě, 