try:
    length = int(input("length:"))
    width = int(input("width:"))
    print("area:{}".format(length*width))
except ValueError:
    #The bottom line is to simply tell the user if the input is not a number.
    print("The value is not a number.")