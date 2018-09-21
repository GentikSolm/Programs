firstCall = input("Please Enter a string!\n::\t")
def stringEx(UserIn):
    print(UserIn)
    print(UserIn.upper())
    print(UserIn.lower())
    print(UserIn[::-1])
    for i in UserIn:
        print(i)
    print("------")
    for i in UserIn[::-1]:
        print(i)
    print("------")
    print("This is a formated string {}".format(UserIn))
    print("This is not a formated string " + UserIn)
    print(UserIn.split(UserIn[0])) #RETURNS ARRAY
    print(UserIn.strip()) #Removes white space from front and back
    print(len(UserIn)) #Returns # of charaters in string
    print(UserIn.replace(UserIn[0], UserIn[1])) #replaces things
stringEx(firstCall)

#Array vs list:
#Array stores large data easy and can do arithmatic
#list is easier to write but cannot do arithmatic and is not so data compact
#myArray = array([1, 2, 3])
#myList = [1, 2, 3]
