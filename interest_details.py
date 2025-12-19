def get_details(interest_type):

    while True:

        principal = input("Enter the principal amount: ")
        
        try:
            principal = float(principal)
            break   

        except Exception:
            print("Please enter a valid principal amount!")
            continue

    while True:

        rate = input("Enter the rate of interest (per annum): ")
        
        try:
            rate = float(rate)
            break   

        except Exception:
            print("Please enter a valid rate of interest!")
            continue

    if interest_type == "CI":

        print("\nChoose compounding frequency:")
        print("1. Annually")
        print("2. Half-Yearly")
        print("3. Quarterly")
        print("4. Monthly")

        while True:
            
            choice = input("Select an option(1-4): ")
            
            if choice == '1':
                frequency = 1
                break

            elif choice == '2':
                frequency = 2
                break

            elif choice == '3':
                frequency = 4
                break

            elif choice == '4':
                frequency = 12
                break
            
            else:
                print("Please enter a valid choice!")

    while True:

        time_value = input("Enter the time: ")

        try:
            time_value = float(time_value)
            break

        except Exception:
            print("Please enter a valid number!")

    print("\nUnit of time: ")
    print("1. Years")
    print("2. Months")

    while True:

        option = input("Choose the unit (1-2): ")

        if option == "1":
            time_years = time_value
            break

        elif option == "2":
            time_years = time_value / 12
            break

        else:
            print("Please enter a valid choice!")

    if interest_type == "SI":
        return principal, rate, time_years
    
    elif interest_type == "CI":
        return principal, rate, time_years, frequency