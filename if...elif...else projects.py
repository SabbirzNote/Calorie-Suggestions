print("This is a app for suggesting calorie requirement for chilrens based on gender and age.Please provide me your gender:")
gender = input()
def female():
    print("Provide me your age:")
    age = int(input())
    if age < 2:
        print("|YOu should consult doctors per day!")
    elif age<4:
        print("YOu need 1000-1400 caloriess per day!")
    elif age<8:
        print("You need 1200-1800 calories per day!")
    elif age<13:
        print("You need 1400-2200 calories per day!")
    elif age<=18:
        print("You need 1800-2200 calories per day!")

    else:
        print("Consult Doctor i cannot provide information for this age")
    

def male():
    print("Provide me your age:")
    age = int(input())
    if age < 2:
        print("|YOu should consult doctors per day!")
    elif age<4:
        print("YOu need 1000-1600 caloriess per day!")
    elif age<8:
        print("You need 1200-2000 calories per day!")
    elif age<13:
        print("You need 1400-2600 calories per day!")
    elif age<=18:
        print("You need 1800-3200 calories per day!")

    else:
        print("Consult Doctor i cannot provide information for this age")

if gender == "male":
    x = male()
    print(x)
elif gender == "female":
    y = female()
    print(y)
else:
    print("Provide a valid gendar")