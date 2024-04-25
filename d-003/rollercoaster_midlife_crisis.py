height = int(input("How tall are you (in cm)?\n"))
if height >= 120:
    bill = 0
    print("Great, you're tall enough to ride!")
    age = int(input("How old are you?\n"))
    if age <= 12:
        # Child ticket (12 and under)
        print("A child ticket is $5")
        bill += 5
    elif age < 18:
        # Youth ticket (between 12 and 18)
        print("A youth ticket is $8")
        bill += 8
    if age >= 45 and age <= 55:
        # Mid-life Crisis ticket (i.e. Free)
        print("You're having a mid-life crisis, you ride for FREE!")
    else:
        # Adult ticket (over 18)
        print("An adult ticket is $12")
        bill += 12
    
    photo = input("Do you want a photo? Type 'Y' or 'N'\n").upper()
    if photo == 'Y':
        bill += 3
        
    print(f"Your total ticket price is: ${bill}")
else:
    print("Sorry, you're too small to ride.")