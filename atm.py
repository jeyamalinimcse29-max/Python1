balance = 10000
correct_pin = "1234"

print("****Welcome to ATM ****")

pin = input("Enter your PIN: ")

if pin == correct_pin:
    print("Login Successful!\n")
    
    while True:
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            print("Your current balance is:", balance)
        
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            print("Amount deposited successfully!")
            print("Updated balance:", balance)
        
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print("Please collect your cash.")
                print("Remaining balance:", balance)
            else:
                print("Insufficient balance!")
        
        elif choice == "4":
            print("Thank you for using ATM. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.")

else:
    print("Incorrect PIN! Access Denied.")
