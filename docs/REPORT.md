Project Report: Simple Banking System in Python
Project Title: Console-Based Banking Management System
Developed By: [Rajkumar Namdev REGI: 26MIP10005]
Programming Language: Python 3.item
Files Included: account.py, banking.py, main.py, user_interface.py, README.md
1. Project Overview & Motivation
The purpose of this project is to simulate routine bank transactions through a lightweight terminal program.
In everyday banking, standard tasks include opening a new account, depositing cash, making withdrawals, and checking account balance.
The goal was to build a functional system using fundamental Python constructs- lists, dictionaries, loops, and functions without relying on heavy databases or external third-party libraries.
The main development priorities were separating the code cleanly into distinct modules and preventing application crashes caused by improper user input.
2. Project Architecture & File Structure
Instead of placing the entire logic into one long file, the source code is divided across three focused Python modules and a documentation file:
account.py (Data Management): Handles user data, including registering new accounts, validating 4-digit PINs, and searching for accounts in the records list.
banking.py (banking Engine): Contains business logic for money operations, such as depositing funds, validating withdrawals, checking PINs, and updating account balances.
user_interface.py (User Interface): Runs the command-line menu loop, displays user choices (1 to 6), and connects menu selections to backend functions.
README.md (Documentation): Outlines instructions for cloning the repository and running the program in the terminal.
3. Detailed Working of Modules
A. Account Management (account.py)
Data Storage: All account data is stored in runtime memory using a global list: accounts = []. Each user record is created as a Python dictionary containing account_number, name, pin, and an opening balance initialized to 0.0.
Sequential Account Numbers: Account numbers are generated automatically via the formula 1001 + total(accounts). This assigns consecutive numbers starting from 1001, 1002, and onward without manual input.
PIN Validation: Prompts the user to set a security code and confirms that it consists of exactly four numeric digits (total(pin) == 4 and pin.isdigit()).
Helper Function (find_account): Loops through the global list and returns the matching user dictionary if the provided account number exists, or None if not found.
Account Details Display (account_details): Requests an account number, catches non-numeric inputs using try-except ValueError, and displays the name, account number, and balance while keeping the PIN hidden.
B. banking Engine (banking.py)
Deposit (deposit_money): Finds the account using find_account(). A PIN is not required for deposits to allow straightforward counter crediting. It verifies that the deposit amount is greater than zero (amt > 0) before updating the balance to two decimal places.
Withdrawal Safety (withdraw_money): Requires the customer to enter their 4-digit PIN. If incorrect, the transaction aborts.
Overdraft Prevention: If the requested withdrawal amount exceeds the current balance (amt > balance), the transaction is stopped with an "Insufficient balance!" warning.
Balance Inquiry (check_balance): Prompts for the account number and PIN. Upon successful verification, it displays the account holder's name and active balance.
C. User Interface Loop (user_interface.py)
Continuous Execution: An infinite while True loop keeps the application active so users can perform multiple banking tasks in a single session without restarting the program.
Menu Routing: Offers numerical choices 1 through 6. If a user enters an unlisted number or character, an "Invalid choice!" prompt asks them to re-enter a valid option.
Clean Termination: Selecting option 6 executes a break statement to close the program cleanly with an exit message.
Standard Invocation: Uses if __name__ == "__main__": main() to ensure the interface executes only when the script is run directly.
4. Input Validations & Exception Handling
To ensure runtime stability, key input checks are implemented throughout the code:
Empty Name Check: Uses .strip() to prevent blank or whitespace-only names during account creation.
Non-Numeric Input Protection: Prompts requiring numeric values (account numbers and transaction amounts) are protected by try-except ValueError blocks, preventing termination if letters or symbols are typed.
Negative Value Guard: Both deposit and withdrawal routines reject zero and negative numbers.
PIN Requirement: Enforces a strict 4-digit numeric format and blocks unauthorized access to funds or balance details.
Project Report: Simple Banking System in Python
Project Title: Console-Based Banking Management System
Developed By: [Your Name / Roll Number]
Programming Language: Python 3
Files Included: account.py, transactions.py, main.py, README.md
1. Project Overview & Motivation
The purpose of this project is to simulate routine bank transactions through a lightweight terminal program.
In everyday banking, standard tasks include opening a new account, depositing cash, making withdrawals, and checking account balances.
The goal was to build a functional system using fundamental Python constructs—lists, dictionaries, loops, and functions—without relying on heavy databases or external third-party libraries.
The main development priorities were separating the code cleanly into distinct modules and preventing application crashes caused by improper user input.
2. Project Architecture & File Structure
Instead of placing the entire logic into one long file, the source code is divided across three focused Python modules and a documentation file:
account.py (Data Management): Handles user data, including registering new accounts, validating 4-digit PINs, and searching for accounts in the records list.
transactions.py (Transaction Engine): Contains business logic for money operations, such as depositing funds, validating withdrawals, checking PINs, and updating account balances.
main.py (User Interface): Runs the command-line menu loop, displays user choices (1 to 6), and connects menu selections to backend functions.
README.md (Documentation): Outlines instructions for cloning the repository and running the program in the terminal.
3. Detailed Working of Modules
A. Account Management (account.py)
Data Storage: All account data is stored in runtime memory using a global list: accounts = []. Each user record is created as a Python dictionary containing account_number, name, pin, and an opening balance initialized to 0.0.
Sequential Account Numbers: Account numbers are generated automatically via the formula 1001 + total(accounts). This assigns consecutive numbers starting from 1001, 1002, and onward without manual input.
PIN Validation: Prompts the user to set a security code and confirms that it consists of exactly four numeric digits (total(pin) == 4 and pin.isdigit()).
Helper Function (find_account): Loops through the global list and returns the matching user dictionary if the provided account number exists, or None if not found.
Account Details Display (account_details): Requests an account number, catches non-numeric inputs using try-except ValueError, and displays the name, account number, and balance while keeping the PIN hidden.
B. Transactions Engine (transactions.py)
Deposit (deposit_money): Finds the account using find_account(). A PIN is not required for deposits to allow straightforward counter crediting. It verifies that the deposit amount is greater than zero (amt > 0) before updating the balance to two decimal places.
Withdrawal Safety (withdraw_money): Requires the customer to enter their 4-digit PIN. If incorrect, the transaction aborts.
Overdraft Prevention: If the requested withdrawal amount exceeds the current balance (amt > balance), the transaction is stopped with an "Insufficient balance!" warning.
Balance Inquiry (check_balance): Prompts for the account number and PIN. Upon successful verification, it displays the account holder's name and active balance.
C. User Interface Loop (main.py)
Continuous Execution: An infinite while True loop keeps the application active so users can perform multiple banking tasks in a single session without restarting the program.
Menu Routing: Offers numerical choices 1 through 6. If a user enters an unlisted number or character, an "Invalid choice!" prompt asks them to re-enter a valid option.
Clean Termination: Selecting option 6 executes a break statement to close the program cleanly with an exit message.
Standard Invocation: Uses if __name__ == "__main__": main() to ensure the interface executes only when the script is run directly.
4. Input Validations & Exception Handling
To ensure runtime stability, key input checks are implemented throughout the code:
Empty Name Check: Uses .strip() to prevent blank or whitespace-only names during account creation.
Non-Numeric Input Protection: Prompts requiring numeric values (account numbers and transaction amounts) are protected by try-except ValueError blocks, preventing termination if letters or symbols are typed.
Negative Value Guard: Both deposit and withdrawal routines reject zero and negative numbers.
PIN Requirement: Enforces a strict 4-digit numeric format and blocks unauthorized access to funds or balance details.
5. Current Limitations & Future Improvements
Current Limitation: Data is stored in memory via a Python list, meaning all created accounts and transaction records reset once the terminal is closed.
Planned Enhancements:
Add persistent storage using an SQLite database or local JSON/CSV file handling.
Implement an inter-account transfer function to allow balance transfers between two users.
Replace the command-line interface with a desktop Graphical User Interface (GUI) using Tkinter

Project Presentation Report: Working Demonstration of Simple Banking System
Project Name: Simple-Banking-system
Main Execution Script: user_interface.py
Environment: Command Prompt/Terminal
Language: Python 3
1. Program Execution & Entry Point
2.  Navigated to the project directory simple-banking-system inside the terminal.
  Executed the main user interface file directly using the command:
   python user_interface.py

Upon pressing Enter, the system instantly initialized and rendered the main command-line interface menu.
2. Main Menu Options
The application loaded the following operational choices:
 Create Account: Registers a new user with personal details and a security PIN.
 Account Details: Displays basic information of an existing registered account.
 Check Balance: Verifies the active available balance.
Deposit Money: Credits funds into a specified account.
  Withdraw Money: Debits funds from the account after PIN authentication.
  Exit: Safely terminates the running application.
3. Step-by-Step Live Demonstration
Step A: Account Creation (Choice 1)
  Action Taken: Selected Option 1 from the main menu.
  Input Provided:
   * Enter your name: rajkumar
   * Set your PIN: 1234
  Internal Logic:
     The program verified that the name string was non-empty.
    Validated that the PIN is strictly a 4-digit numeric string.
     Auto-assigned the initial sequential account number using the formula 1001 + total(accounts).
  System Output Received:
   Account created successfully!
Your account number is: 1001
```[span_32](start_span)[span_32](end_span)

Step B: Continuous Menu Loop & Record Retrieval (Choice 2)
  Loop Continuity: Instead of terminating, the program maintained its while True loop and re-displayed the main menu cleanly.
 Action Taken: Selected Option 2 (Account Details).
  Input Provided:
 Enter account number: 1001
  Internal Logic:
    The helper function find_account(1001) searched the in-memory customer list and returned the matching dictionary record.
  System Output Received:
   Account Details
Name: rajkumar
Account Number: 1001
Balance: 0
  [span_41](start_span)[span_41](end_span)

  Security & Verification: The system successfully retrieved the customer's name, assigned account number, and default opening balance (0), while keeping the security PIN hidden from display.
4. Presentation Summary of the Output
  Executing python user_interface.py serves as the primary controller for the application.
  Account creation and record searching completed with zero runtime exceptions.
  The terminal workflow proves that user inputs are processed, verified, and displayed in real-time as intended.
