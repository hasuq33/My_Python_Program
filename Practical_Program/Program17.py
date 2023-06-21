# This python program that computes the net amount of
# a bank account based a transaction log from console input.
# The transaction log format is shown as following:
# D 100
# W 200

# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

def main():
    balance = 0
    while True:
        usr = input("Press 'W' for withdrawl , 'D' for Deposit , 'C' for check the balance and 'Q' for exit:  ").lower()

        if usr == 'd':
            amount = int(input("Enter the amount to deposit: "))
            balance += amount
            print(f"You have succefully deposited amount {amount}")
        
        if usr == 'w':
            if balance <= 0:
                print("Your account has insufficient funds to withdraw.Please deposit amount ")
                return main()
            elif balance > 0:
                amount = int(input("Enter the amount to withdraw: "))
                balance -= amount 
                print(f"You successfully withdraw {amount}")  
        if usr == 'c':
            print(f"You have {amount} funds in your account")         
        
        if usr == 'q':
            print(balance)
            break

if __name__ == '__main__':
    main()