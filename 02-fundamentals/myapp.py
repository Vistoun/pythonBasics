import physics 

print("Vypočet gravitační síly na Zemi a Měsici při hmotnosti(Kg):")
hmotnost = float(input())
print(f"Gravitčaní síla na Zemi a na Měsíci při hmotnosti {hmotnost}Kg je {physics.gravityForce_earth(hmotnost)} N na Zemi a {physics.gravityForce_moon(hmotnost)} N na Měsíci")



print("Za kolik sekund jsi slyšel zvuk ohňostroje?")
cas = float(input())
print(f"Ohňostroj je od tebe vzdálený {physics.vypocetDrahy(cas)} metrů")

print("Urči hmotnost libovolné hmoty v Kg")
hmota = float(input())
print(f"Množství energie v {hmota}Kg libovolné hmoty je {physics.energie(hmota)} J")