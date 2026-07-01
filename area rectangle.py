try:
    length = int(input("length:"))
    width = int(input("width:"))
    print("area:{}".format(length*width))
except ValueError:
    print("The value is not a number.")