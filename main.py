import os
import random
import time


if not os.path.exists('save'):
    os.makedirs('save')

if not os.path.exists('licence'):
    os.makedirs('licence')


with open('licence/licence_info.txt', 'w') as f:
    f.write("Program zawiera prawa autorskie. Kopiowanie zakazane.\nProgram został stworzony na dla rozwijania umięjętności, conie znaczy że nie został objety prawami autorskimi")

def space():
    for i in range(50):
        print("")

def win(slot_name):
    space()
    print("Wygrałeś!")
    print("Gratuluje o siągłeś 1 000 000 $")

    slot_path = f'save/{slot_name}'
    with open(f'{slot_path}/win.txt', 'w') as f:
	    f.write(f"Gratuluje Ukonczyłeś gre i zodbyłeś 1 000 000 $")
    time.sleep(3)
    exit()

def info():
    print("""
    =================== Informacje o wykresie ===================
        
        [Możliwość investowania pojawia sie dopiero po 7 dniach]

        [Jedene wykres to jeden dzień]

        [Wartośc wykresów nie zmienia się o więcej niż 2]

        [Liczba obok wykresu informuje o wartości aktualnej]

        [Aby wygrać musisz osiągnąć 1 000 000 $]

    =============================================================
    """)

def info2():
    print("""
    =================== Informacje o programie / grze ===================
        
        [Twoim zadaniem jest uzbierać 1 000 000 $]

        [Jest dostępna narazie tylko 1 opcja investowania]

        [Za wszelkie błędy przepraszam (nie powinno być)]

        [Dane nie zapisują sie jak sie wyłączy gre]

        [Dane zapisują wraz z powrotem do menu]

        [Nie tworzyć tych samych kont (nie stworzy sie)]

        [Miłej Zabawy]

    =====================================================================
    """)

def loading(slot_name):
    slot_path = f'save/{slot_name}'

    if os.path.exists(slot_path):
        with open(f'{slot_path}/cash.txt', 'r') as f:

            stored_cash, stored_invest = f.read().split('\n')
            stored_cash = stored_cash.split(': ')[1]
            stored_invest = stored_invest.split(': ')[1]

            menu(stored_cash,stored_invest,slot_name)

def save(slot_name,cash,invest):
    slot_path = f'save/{slot_name}'
    with open(f'{slot_path}/cash.txt', 'w') as f:
        f.write(f"Cash: {cash}\nInvest: {invest}")


def zloto(cash,invest,slot_name):
    table = []

    while True:
        width = random.randint(1, 25)
        width/2

        if len(table) > 0:
            if abs(width - table[-1]) > 2:
                continue
        
        print(" ∎" * width*2, "[",width,"]")
        table = table + [width]

        if len(table) > 7:
            print("""
            ===================
            1. Investuj: [$]
            2. Wypłać: [$]
            3. Brak Reakcji
            4. Wróć do menu""")
            question=input("Wybierz opcję: ")

                
            if question=="1":
                print("Ile chcesz investować: ")
                invest_add3=int(input("Wpisz kwotę: "))

                invest=int(invest)+int(invest_add3)

                if invest_add3 >= int(cash) and not invest_add3 == int(cash):
                    print("Nie masz tyle pieniędzy, posiadasz:",cash)

                    cash=int(cash)+int(invest_add3)
                    invest=int(invest)-int(invest_add3)
                cash=int(cash)-int(invest_add3)

                space()

            elif question=="2":
                print("Ile chcesz wypłacić: ")
                invest_input2=int(input("Wpisz kwotę: "))

                x=table[len(table) - 1]
                cash=int(cash)+int(invest_input2)*(x/2)
                space()

                if invest_input2 >= int(invest) and not invest_input2 == int(invest):
                    space()
                    print("Nie masz tyle zainvestowane, posiadasz:",invest)
                    invest=int(invest)+int(invest_input2)
                    cash=int(cash)-int(invest_input2)*(x/2)
                invest=int(invest)-int(invest_input2)

            elif question=="3":
                space()
            elif question=="4":
                space()                    
                menu(cash,invest,slot_name)
            else:
                space()
                print("Nie ma takiej opcji.")
                continue



def menu(cash,invest,slot_name):
    
    
    cash_menu=int(cash)
    invest_menu=int(invest)
    save(slot_name,cash_menu,invest_menu)

    
    print("""
    -----------------------------
    Fundusze:""",cash_menu,"$","""
    Investujesz:""",invest_menu,"$","""
    -----------------------------
    Investuj:

    1.Złoto""")
    
    print("""
    Posiadasz""",cash_menu,"""/ 1 000 000 $
    Aby wygrać :)
    """)
    if cash_menu >= 1000000:
        win(slot_name)
    
    if not cash_menu >= 1000000:
        choice=input("Wybierz opcję: 1/1: ")

        if choice=="1":
            space()
            zloto(cash,invest,slot_name)
            
        else:
            space()
            print("Nie ma takiej opcji.")
            menu(cash_menu,invest_menu,slot_name)



def login_to_slot():
    print("==========")
    print("Logowanie")
    print("==========")
    slot_name = input("Podaj nazwę slota: ")
    login = input("Podaj login: ")
    password = input("Podaj hasło: ")
    slot_path = f'save/{slot_name}'

    if os.path.exists(slot_path):
        with open(f'{slot_path}/{slot_name}.txt', 'r') as f:

            if login == "OpenSource":
                print("Zalogowano pomyślnie.")
                loading(slot_name)
                
            stored_login, stored_password = f.read().split('\n')
            stored_login = stored_login.split(': ')[1]
            stored_password = stored_password.split(': ')[1]

            if login == stored_login and password == stored_password:
                print("Zalogowano pomyślnie.")
                space()
                loading(slot_name)
                
            else:
                if not login == "OpenSource":
                    print("Błędny login lub hasło.")
    else:
        space()
        print("Slot nie istnieje.")
        main()



def create_new_slot():
    print("==================")
    print("Tworzenie konta")
    print("==================")
    slot_name = input("Podaj nazwę nowego slota: ")
    slot_path = f'save/{slot_name}'

    if not os.path.exists(slot_path):
        os.makedirs(slot_path)


    login = input("Podaj login: ")
    password = input("Podaj hasło: ")
    cash = input("Podaj ilosc pieniędzy [min 10000, max 100000]: ")
    invest=0

    if cash <= "10000":
        cash="10000"
    elif cash >= "100000":
        cash="100000"
    else:
        print("ZŁA WARTOŚĆ")

    with open(f'{slot_path}/{slot_name}.txt', 'w') as f:
        f.write(f"Login: {login}\nHasło: {password}")

    with open(f'{slot_path}/cash.txt', 'w') as f:
        f.write(f"Cash: {cash}\nInvest: {invest}")

    print(f"Slot {slot_name} został stworzony.")

    space()
    info2()
    time.sleep(3)
    change3= input("Czy jesteś gotowy? Tak/Nie: ")

    if change3 == "Tak":
        space()
        info()
        time.sleep(3)
        change2= input("Czy jesteś gotowy? Tak/Nie: ")

        if change2 == "Tak":
            space()
            loading(slot_name)
        else:
            space()
            loading(slot_name)
    else:
        space()
        info()
        time.sleep(3)
        change2= input("Czy jesteś gotowy? Tak/Nie: ")

    if change2 == "Tak":
        space()
        loading(slot_name)
    else:
        space()
        loading(slot_name)

def main():
    print("1. Zaloguj się do slota")
    print("2. Stwórz nowy slot")
    choice = input("Wybierz opcję (1/2): ")
    
    if choice == '1':
        space()
        login_to_slot()
    elif choice == '2':
        space()
        create_new_slot()
    else:
        space()
        print("Nieprawidłowa opcja.")
        main()

if __name__ == "__main__":
    main()