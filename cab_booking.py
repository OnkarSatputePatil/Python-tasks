import random

while True:
    print("1. Book Ride")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("1. Auto - ₹12/km")
        print("2. Sedan - ₹18/km")
        print("3. SUV - ₹25/km")

        cab_choice = input("Enter cab type: ")

        if cab_choice == "1":
            cab_type = "Auto"
            rate = 12
        elif cab_choice == "2":
            cab_type = "Sedan"
            rate = 18
        elif cab_choice == "3":
            cab_type = "SUV"
            rate = 25
        else:
            print("Invalid cab choice.")
            continue

        print("1. Mumbai Central to Dadar - 7 km")
        print("2. Thane to Mulund - 9 km")
        print("3. Andheri to Bandra - 12 km")

        route_choice = input("Enter route number: ")

        if route_choice == "1":
            source = "Mumbai Central"
            destination = "Dadar"
            distance = 7
        elif route_choice == "2":
            source = "Thane"
            destination = "Mulund"
            distance = 9
        elif route_choice == "3":
            source = "Andheri"
            destination = "Bandra"
            distance = 12
        else:
            print("Invalid route choice.")
            continue

        fare = rate * distance

        print("Cab Type:", cab_type)
        print("Source:", source)
        print("Destination:", destination)
        print("Distance:", distance, "km")
        print("Rate: ₹", rate, "/km")
        print("Total Fare: ₹", fare)

        print("1. Confirm & Share OTP")
        print("2. Cancel Ride")

        confirm = input("Enter your choice: ")

        if confirm == "1":
            otp = random.randint(1000, 9999)
            print("Booking confirmed!")
            print("Your OTP is:", otp)
            print("OTP has been shared with you.")
            print("Once OTP is shared, the ride cannot be cancelled.")

        elif confirm == "2":
            print("Ride cancelled successfully.")
            print("No OTP was shared.")

        else:
            print("Invalid choice. Ride cancelled.")

    elif choice == "2":
        print("Thank you for using Cab Booking Chatbot!")
        break

    else:
        print("Invalid menu choice.")