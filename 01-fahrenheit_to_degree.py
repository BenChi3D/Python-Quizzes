def fah_to_deg(x):
    if x > 0:
        ans = 5 * (x-32) / 9 #  we do this because integer division truncates
        return ans
    else:
        print("please input a positive number, cannot evaluate negative numbers")
