import csv

from caesar import caesar_encrypt

def encrypt_single_pass(filename: str) -> None:
    """TODO: Parte 1."""
    with open(filename, "r") as Archivo:
        contraseña= Archivo.readline().strip()
    contraseña_incriptada=caesar_encrypt(contraseña)

    with open(filename, "w") as Archivo:
        Archivo.write(contraseña_incriptada)


def encrypt_passwords_in_file(filename: str) -> None:
    """TODO: Parte 2."""
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        
        for fila in reader:
            print(fila)

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        filas = list(reader)

    for i in range(1, len(filas)):
        if not filas[i]:
                continue
        filas[i][2] = caesar_encrypt(filas[i][2])

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(filas)


def change_password(filename: str, website: str, password: str) -> bool:
    """TODO: Parte 3."""
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        filas = [fila for fila in reader if fila]
    encontrado = False

    for i in range(1, len(filas)):
            if filas[i][0] == website:
                filas[i][2] = caesar_encrypt(password)
                encontrado = True
                break
    if not encontrado:
        return False
            
    with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(filas)
    return True

def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    """TODO: Parte 4."""
    encrypted = caesar_encrypt(password)
    
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([website_name, username, encrypted])
