import chat.chat as chat

def start():
    show_logo()
    show_loading_screen()

    name = get_username()

    message = show_welcome_message(name)
    print(message)

    running = True
    while running:
        show_main_menu()
        choice = get_menu_choice()
        running = process_menu_choice(choice, name)


def show_logo():
    print("JARVIS AI")
def show_loading_screen():
    print("Laden... Bitte warten.")
def show_welcome_message(name):
    if name == "admin":
        return "Willkommen zurück, Administrator!"
    return "Willkommen zurück, " + name + "!"

def get_username():
    name = input("Bitte geben Sie Ihren Namen ein: ")

    while name == "":
        print("Name kann nicht leer sein.")
        name = input("Bitte geben Sie Ihren Namen ein: ")
    return name

def show_main_menu():
    print()
    print("======================")
    print("      JARVIS AI")
    print("======================")
    print()
    print("1. Chat")
    print("2. Rechner")
    print("3. Einstellungen")
    print("4. Beenden")

def get_menu_choice():
    choice = input("Bitte wählen Sie eine Option (1-4): ")
    while choice not in ["1", "2", "3", "4"]:
        print("Ungültige Auswahl. Bitte wählen Sie eine gültige Option (1-4).")
        choice = input("Bitte wählen Sie eine Option (1-4): ")
    return choice

def process_menu_choice(choice, name):
    if choice == "1":
        chat.start_chat(name)
        return True
    elif choice == "2":
        print("Öffne Rechner...")
        return True
    elif choice == "3":
        print("Öffne Einstellungen...")
        return True
    elif choice == "4":
        print("Beende JARVIS AI. Auf Wiedersehen!")
        return False