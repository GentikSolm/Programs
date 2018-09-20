print("Hello, Please input your name!")
UserIn = input()
def nameChange(name):
    print("Hello {}!".format(name.upper()))
    print(name[::-1])
nameChange(UserIn)
