from account import create_account, account_details
from banking import check_balance, deposit_money, withdraw_money


def show_menu():
    print("\n===== SIMPLE BANKING SYSTEM =====")
    print("1. Create Account")
    print("2. Account Details")
    print("3. Check Balance")
    print("4. Deposit Money")
    print("5. Withdraw Money")
    print("6. Exit")


def start_program():
    while True:
        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            account_details()

        elif choice == "3":
            check_balance()

        elif choice == "4":
            deposit_money()

        elif choice == "5":
            withdraw_money()

        elif choice == "6":
            print("Thank you for using the banking system.")
            break

        else:
            print("Invalid choice. Please try again.")


start_program()
