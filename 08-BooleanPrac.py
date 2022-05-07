def checkString():
    word = input("please input password:\n")
    if len(word) == 8 or len(word) > 8:
        print("This is a good password")
    elif len(word) >= 15:
        print("The password is too long")
        checkString()
    else:
        print("Password is too short, please password should be 8 character or more, but less than 15 characters.")
        checkString()

checkString()
