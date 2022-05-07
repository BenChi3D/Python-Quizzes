def count_a():
    count = 0
    word = input("enter word to be counted:\n")
    for ch in word:
        if ch == "a":
            count ++ 1
    print(count)

count_a()
