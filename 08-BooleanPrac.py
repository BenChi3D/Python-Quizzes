def checkString(word):
    if len(word) == 8 or len(word) > 8:
        print("This is a good password")
    elif len(word) > 15:
        print("The password is too long")
    else:
        print("Password is too short, please password should be 8 character or more, but less than 15 characters.")
