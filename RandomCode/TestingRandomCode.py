mystring = "Hello one two three"
def test():
    myList = mystring.split(" ")
    myList.pop()
    a = myList[0]
    for i in myList[1:]:
        a +=" "+ i
    print(a)
test()
