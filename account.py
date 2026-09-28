# Module 1 - Account Management

accounts = []

def create_account():
    name = input("Enter your name: ")
    pin = input("Set your PIN: ")

    account_number = 1001 + len(accounts)

    account = {"account_number": account_number,
                  "name": name,
                   "pin": pin,
               "balance": 0}

    accounts.append(account)

    print("\nAccount created successfully!")
    print("Your account number is:", account_number)

def account_details():
    account_number = int(input("Enter account number: "))

    for account in accounts:
        if account["account_number"] == account_number:
            print("\nAccount Details")
            print("Name:", account["name"])
            print("Account Number:", account["account_number"])
            print("Balance:", account["balance"])
            return

    print("Account not found")


create_account()
account_details()
