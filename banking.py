from account import accounts

def check_balance():
    account_number = int(input("Enter account number: "))

    for account in accounts:
        if account["account_number"]  ==account_number:
            print("Your balance is:", account["balance"])
            return

    print("Account not found")

def deposit_money():
    account_number = int(input("Enter account number: "))

    for account in accounts:
        if account["account_number"]  ==account_number:
            amount = float(input("Enter amount to deposit: "))

            if amount > 0:
                account["balance"] += amount
                print("Money deposited successfully")
                print("New balance:", account["balance"])
            else:
                print("Enter a valid amount")
            return

    print("Account not found")

def withdraw_money():
    account_number = int(input("Enter account number: "))

    for account in accounts:
        if account["account_number"]  ==account_number:
            amount = float(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Enter a valid amount")
            elif amount > account["balance"]:
                print("Insufficient balance")
            else:
                account["balance"] -= amount
                print("Money withdrawn successfully")
                print("Remaining balance:", account["balance"])
            return

    print("Account not found")
