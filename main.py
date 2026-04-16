from password_manager import add_login, change_password, encrypt_passwords_in_file


def main() -> None:
    """TODO: Parte 5 - programa principal interactivo."""
    nombre_de_archivo=input("Enter the CSV file name:\n")
    encrypt_passwords_in_file(nombre_de_archivo)

    while True:
        print("Options: (1) Change Password, (2) Add Password, (3) Quit:")
        option = input()

        if option == '1':
            user_input = input("Enter the website and the new password:\n")
            parts = user_input.split()
            
            if len(parts) < 2:
                print("Input is in the wrong format!")
                continue
            website, password = parts
            
            if len(password) < 12:
                print("Password is too short!")
                continue
            
            result = change_password(nombre_de_archivo, website, password)
            
            if not result:
                print("Website not found! Operation failed.")
            else:
                print("Password changed.")
        elif option == '2':
            user_input = input("Enter the website, username, and password:\n")
            parts = user_input.split()
            
            if len(parts) < 3:
                print("Input is in the wrong format!")
                continue
            
            website, username, password = parts
            
            if len(password) < 12:
                print("Password is too short!")
                continue
            
            add_login(nombre_de_archivo, website, username, password)
            print("Login added.")
        elif option == '3':
            break
        else:
            print("Invalid option selected!")


if __name__ == "__main__":
    main()
