
# Funktion för att lägga till två tal
def add(x, y):
    return x + y

# Funktion för att subtrahera två tal
def subtract(x, y):
    return x - y

# Funktion för att multiplicera två tal
def multiply(x, y):
    return x * y

# Funktion för att dividera två tal
def divide(x, y):
    if y == 0:
        return "Fel! Kan inte dividera med noll."
    else:
        return x / y

# Huvudfunktionen för miniräknaren
def calculator():
    print("Välj operation:")
    print("1. Addition (Lägg till)")
    print("2. Subtraktion (Dra ifrån)")
    print("3. Multiplikation (Gånger)")
    print("4. Division (Dela)")

    # Användaren väljer en operation
    choice = input("Ange ditt val (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Ange första talet:
