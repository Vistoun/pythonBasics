# Funkce v Pythonu
# Funkce provádějící kód


def greet(first_name, last_name):
    print(f"Ahoj {first_name} {last_name}")
    print("To je pozdrav z funkce")


greet("Vladimir", "Putin")

# Funkce vracející hodnotu
def getGreeting(name):
    return f"Ahoj {name}"

print(getGreeting("Milos"))


# Klíčové argumenty, argument s výchozí hodnotou
def increment(number, by=1):
    return number + by


print(increment(10, by=6))

# Funkce s *args - předání argumentu jako list

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))

# Funkce s **args - předání argumentu jako dictionary
def save_user(**user):
    print(f"id={user['id']} {user}")


save_user(id=1, name="Karel", age=19, student=True)

# Globální a lokální proměnné
message = "Globální proměnná"

def send_message():
    #global message
    message = "Lokální proměnná"


send_message()
print(message)
