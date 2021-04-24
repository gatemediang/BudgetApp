database = { }


class Budget:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def deposit(amount, balance):
        balance += amount
        return balance

    def check_balance(db):
        for categ, balance in db.items():
            print(categ, balance)

    def withdraw(category, amount, balance):
        balance -= amount
        return balance

    def transfer(db, option1, amount, option2):
        value1 = db[option1]
        value2 = db[option2]

        db[option1] = int(value1) - amount
        db[option2] = int(value2) + amount
        return db



def init():
    print('=== **** Welcome to the Home Budget App**** ===\n')
    menu()



def menu():
    try:

        user = int(input('\n=== ****What would you like to do?**** ===\nPress (1) To create Food Budget\nPress (2) To create Clothing Budget\nPress (3) To create Entertainment Budget\nPress (4) To check your budget balance\nPress (5) To transfer money between budgets\nPress (6) To deposit into Budget Category of choice\nPress (7) to withdraw from Budget Category of choice\nPress (8) To quit \n'))
    except:
        print('Invalid input')
        menu()

    if (user == 1):
        category = 'Food'
        amount = int(input("Enter your budget amount \nNGN."))
        category_1 = Budget(category, amount)
        database[category] = amount
        print(f'Budget {category} was setup with NGN.{amount}')
        menu()
    elif (user == 2):
        category = 'Clothing'
        amount = int(input("Enter your budget amount \nNGN."))
        category_2 = Budget(category, amount)
        database[category] = amount
        print(f'Budget {category} was setup with NGN.{amount}')
        menu()
    elif (user == 3):
        category = 'Entertainment'
        amount = int(input("Enter your budget amount \nNGN."))
        category_3 = Budget(category, amount)
        database[category] = amount
        print(f'Budget {category} was setup with NGN.{amount}')
        menu()
    elif (user == 4):
        balance()
    elif (user == 5):
        transfer()
    elif(user == 6):
        credit()
    elif(user == 7):
        debit()
    elif (user == 8):
        out()
    else:
        print('Invalid input\n')
        menu()


def debit():
    print("=== ****Withdraw from a created budget**** ===\n")
    print('**** Available Budgets ****')

    for key, value in database.items():
        print(f"-  {key}")

    pick = int(input('\nPress (1) To continue with your debit transaction\nPress (2) To stop debit transaction\n'))
    if (pick == 1):
        category = input("\n**** Select one of the budget categories to withdraw from ****\n")
        if category in database:
            print('Note: You can not withdraw all your budget, at least NGN1 must remain.')
            amount = int(input("Enter amount \nNGN"))
            if amount < database[category]:
                balance = int(database[category])
                new_balance = Budget.withdraw(category, amount, balance)
                database[category] = new_balance
                print(f"NGN.{amount} has been debited from Budget-{category}\nBudget amount remaining NGN.{new_balance}")
                menu()

            else:
                pick = int(input(f'\nBudget {category} is insufficient of the NGN.{amount} required\nThe actual balance {database[category]}\n\nPress (1) To deposit to the budget\nPress (2) To choose the right budget\n'))
                if (pick == 1):
                    amount = int(input("Enter amount \n$"))
                    balance = int(database[category])
                    new_balance = Budget.deposit(amount, balance)
                    database[category] = new_balance
                    print('')
                    print(f"Budgets {category} has been credited with NGN.{amount}\n")
                    debit()

                elif (pick == 2):
                    debit()
                else:
                    print('Invalid option\n')
                    debit()
        else:
          pick = int(input(f'\n****  Budget {category} does not exist! ****\n'))



def credit():
    print("**** Deposit into a budget ****\n")
    print('**** Available Budgets ****')
    for key, value in database.items():
        print(f"-  {key}")

    pick = int(input('\nPress (1) To continue with your deposit transaction\nPress (2) To stop deposit transaction\n'))
    if (pick == 1):
        category = input("Select a budget \n")
        if category in database:
            amount = int(input("Enter amount \nNGN."))
            balance = int(database[category])
            new_balance = Budget.deposit(amount, balance)
            database[category] = new_balance
            print(f'\nBudget {category} is credited with NGN.{amount}\nTotal Budget amount is now NGN.{new_balance}')
            menu()

        else:
            print('')
            pick = int(input(f'Budget {category} does not exist!\n'))


def balance():
    print("*** Getting Your Budget Balance***\n")
    check_bal = Budget.check_balance(database)
    if (check_bal == None):
        print('')
        menu()
    else:
        print(f'${check_bal}')
        menu()

def transfer():
    print('**** Available and Valid Budgets ****')
    for key, value in database.items():
        print(key)
        print('')
    print("**** Transfer Operations ****")
    print('Note: You can not withdraw all your budget, at least NGN.1 must remain.\n')
    from_budget = input("Enter the budget category you are transferring from \n")
    if from_budget in database:
        from_amount = int(input("Enter amount you want to transfer \nNGN."))
        if from_amount < database[from_budget]:
            to_budget = input("Enter destination of funds \n")
            if to_budget in database:
                db = Budget.transfer(database, from_budget, from_amount, to_budget)
                print("")
                print(f"You transferred NGN.{from_amount} from {from_budget} to {to_budget} ")
                for key, value in db.items():
                    print(key, value)
                menu()
            else:
                print(f'\n{from_budget} Budget does not exist, please choose from the valid budget below\n')
                transfer()
        else:
            print(f'You do not have such amount-NGN.{from_amount} in {from_budget} budget')
            transfer()
    else:
        print(f'Budget {from_budget} does not exist\n')

        transfer()

def out():
    try:
        pick = int(input('Are you sure you want to quit?\nPress (1) to quit\nPress (2) to continue\n'))
    except:
        print('Invalid input\n')
        out()

    if (pick == 1):
        print("\nWe hope you had a good budgeting experience, bye for now.")
        quit()
    elif (pick == 2):
        menu()
    else:
        print('Invalid input\n')
        out()

init()