def too_long():
    word = input("enter any word:\n")
    if len(word) > 5:
        return True
    else:
        return False

too_long()
