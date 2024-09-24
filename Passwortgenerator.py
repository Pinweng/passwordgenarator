import random

def generate_password():
    password = ''
    for i in range(8):
        bereich = random.randint(0,2)
        if bereich == 0:
            random_ascii = random.randint(48, 57)  # ASCII-Bereich für Zeichen, die verwendet werden sollen
        elif bereich == 1:
            random_ascii = random.randint(65, 90)
        else:
            random_ascii = random.randint(97, 122)
        password += chr(random_ascii)
    return password

# Beispielaufruf
generated_password = generate_password()
print("Generiertes Passwort:", generated_password)