print("HOSTEL BILLING SYSTEM")

student_name = input("Enter Student Name: ")
room_number = input("Enter Room Number: ")

hostel_fee = float(input("Enter Hostel Fee: "))
mess_charges = float(input("Enter Mess Charges: "))
electricity_charges = float(input("Enter Electricity Charges: "))
other_charges = float(input("Enter Other Charges: "))

total_bill = hostel_fee + mess_charges + electricity_charges + other_charges

print("\nHOSTEL BILL\n")
print("Student Name:", student_name)
print("Room Number:", room_number)
print("\nHostel Fee: ₹", hostel_fee)
print("Mess Charges: ₹", mess_charges)
print("Electricity Charges: ₹", electricity_charges)
print("Other Charges: ₹", other_charges)
print("\nTotal Bill: ₹", total_bill)