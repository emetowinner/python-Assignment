import random
import sqlite3

# Create the database and tables


def database():
    """
        This function creates bank database if it does not exist and define it's table

        >> database()
        >> True or False
    """
    conn = sqlite3.connect('bank.db')
    conn.execute('''CREATE TABLE BankAccount
            (AccountNumber INT PRIMARY KEY     NOT NULL,
            name           TEXT    NOT NULL,
            Phone            INT     NOT NULL,
            emailaddress        CHAR(50),
            balance         REAL);''')

    print("Accounts Table created")

    return True if conn else False

# Autogenerate Account number for each New Account


def open_account():
    customer_name = input("Your Name: ")
    fon = int(input("Your Phone Number: "))
    email = input("Email Adddress: ")
    amnt = float(input("Initial Deposit: "))
    '''Auto Generate Account number'''
    AcctNo = random.randint(1000000000, 9999999999)
    return (AcctNo, customer_name, fon, email, amnt)


def save_account():
    (Accnu, Name, Phone, Email, Amount) = open_account()
    conn = sqlite3.connect('bank.db')
    conn.execute(f"INSERT INTO BankAccount(AccountNumber, name,phone,emailaddress,balance) \
            VALUES (?, ?, ?, ?, ?)", (Accnu, Name, Phone, Email, Amount))
    conn.commit()
    print(Name, "\'s New Account Opened")


def view_customer_list():
    conn = sqlite3.connect('bank.db')
    try:
        cursor = conn.execute(
            "SELECT rowid, AccountNumber, name, phone, emailaddress, balance from BankAccount")
        for row in cursor:
            print("SN = ", row[0])
            print("Account-Number = ", row[1])
            print("Customer-Name = ", row[2])
            print("Phone Number = ", row[3])
            print("Email Address = ", row[4])
            print("Balance = ", row[5], "\n")
    except:
        print('No such files in the database')
        save_account()


def main():
    database()
    print("Welcome, what will you like to do?")
    while True:
        checker = int(
            input("Enter 0 to quit 1 to creat an account 2 to view accounts: "))
        if checker == 1:
            save_account()
        elif checker == 2:
            view_customer_list()
        elif checker == 0:
            print(
                'Don\'t forget to delete the database befor running the script again or comment out line 15-20')
            break
        else:
            raise Exception(
                'This value {} you entered is invalid'.format(checker))


if __name__ == "__main__":
    main()