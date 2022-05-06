def fah_to_deg():
    x = input("enter temperature to be converted to degree celsius:\n ")
    if int(x) > 0:
        ans = (5.0 * (int(x)-32.0)) / 9.0 #  we do this because integer division truncates
        return ans
    else:
        print("please input a positive number, cannot evaluate negative numbers")

fah_to_deg()
