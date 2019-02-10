def testfunc():
    e = 0
    for a in range(10):
        e = e + 1
        print(e)
        if e == 2:
            break
    print("Hello")
    print(e)
testfunc()
