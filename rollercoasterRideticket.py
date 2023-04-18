print("Welcome to the rollercoaster!")
height = int(input("Enter your height in cm"))

bill = 0

if height > 120:
    print("You can ride")
    age = int(input("Enter your age"))
    if age < 12:
        bill=5
        print('Ticket price is $5')
    elif age <= 18:
        bill=7
        print("Ticket price is $7")
    elif age>=45 and age<=55:  #midlife crisis
        print("Have a free ride on us!")
    else:
        bill=12
        print("Ticket price is $12")

    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        bill+=3

    print(f"Your final bill is {bill}")

else:
    print("You cannot ride")




