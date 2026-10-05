age = int(input("Enter your age: "))

if age < 0:
    print("Invalid Age")
elif age >= 18:
    print("Valid Age and Eligible for Voting")
else:
    print("Valid Age but Not Eligible for Voting")