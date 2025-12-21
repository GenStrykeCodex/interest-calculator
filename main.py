# Start building CLI Interest Calculator version 1.1

# importing module to get details of interest
from interest_details import *

# greeting message
print("\nWelcome to Interest Calculator v1.1")

# calculating simple interest
def calculate_SI(p,r,t):

    SI = p*r*t/100  # formula for simple interest
    amount = p + SI # calculate amount
    
    print(f"\nSimple Interest: {round(SI,2)}")
    print(f"Total amount: {round(amount,2)}")


# simple interest calculator menu
def simple_interest_menu():

    while True:
        print("\n|------- SIMPLE INTEREST -------|")
        print("\n1. Start Calculating.")
        print("2. Return to Main Menu.")

        while True:
            choice_2 = input("\nChoose an option (1-2): ")
            
            if choice_2 == "1":

                p,r,t = get_details("SI")
                calculate_SI(p,r,t)

                input("\nPress Enter to continue...")
                break
            
            elif choice_2 == "2":

                print("Returning to the main menu")
                main_menu()
                return

            else:
                print("Please enter a valid choice.")

# calculating compound interest
def calculate_CI(p,r,t,n):

    amount = p*(1+r/(n*100))**(n*t)  # formula for compound amount
    CI = amount - p # formula for compound interest

    print(f"\nCompound Interest: {round(CI,2)}")
    print(f"Total amount: {round(amount,2)}")

# compound interest calculator menu
def compound_interest_menu():

    while True:
        print("\n|------- COMPOUND INTEREST -------|")
        print("\n1. Start Calculating.")
        print("2. Return to Main Menu.")

        while True:
            choice_3 = input("\nChoose an option (1-2): ")
            
            if choice_3 == "1":

                p,r,t,n = get_details("CI")
                calculate_CI(p,r,t,n)

                input("\nPress Enter to continue...")
                break
            
            elif choice_3 == "2":

                print("Returning to the main menu")
                main_menu()
                return

            else:
                print("Please enter a valid choice.")

# compare SI and CI
def compare_SI_CI():
    
    while True:

        print("\n|------- COMPARE INTERESTS -------|")
        print("\n1. Start Calculating.")
        print("2. Return to Main Menu.")

        while True:
            choice_4 = input("\nChoose an option (1-2): ")
            
            if choice_4 == "1":

                p,r,t,n = get_details("CI")

                print("\n[-------- SIMPLE INTEREST --------]")
                calculate_SI(p,r,t)
                print("\n[------- COMPOUND INTEREST -------]")
                calculate_CI(p,r,t,n)

                input("\nPress Enter to continue...")
                break
            
            elif choice_4 == "2":

                print("Returning to the main menu")
                main_menu()
                return

            else:
                print("Please enter a valid choice.")

# home menu
def main_menu():
    
    print("\n|------- MAIN MENU -------|")
    print("\n1. Simple Interest Calculator.")
    print("2. Compound Interest Calculator.")
    print("3. Compare SI and CI.")
    print("4. Exit the Program.")

# main function
def main():

    main_menu()

    run = True
    while run:     # the loop will run until given a valid choice

        choice_1 = input("\nChoose an option (1-4): ")

        if choice_1 == "1": 
            # opens SI calculator menu
            simple_interest_menu()

        elif choice_1 == "2":
            # opens CI calculator menu
            compound_interest_menu()

        elif choice_1 == "3":
            # opens compare interests menu
            compare_SI_CI()

        elif choice_1 == "4":
            # exists the application
            print("Exiting Interest Calculator..")
            run = False
        
        else:
            # if given choice is invalid
            print("Please enter a valid choice!")

    print("Thank you for using our Interest Calulator!")

main()
