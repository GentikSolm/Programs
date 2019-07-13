importList = ["DigPi"]
PaD = __import__('ProjectADay',globals(), locals(),importList)

CallNumDict = {1.1:["DigPi",PaD.DigPi.help,PaD.DigPi.main],}
def run(CallNum):
    pass

def help(CallNum):
    if CallNum == None:
        print("""Here are possible commands:\n\n'List'\t\tLists all files in database and their call number.\n'Help [call number]'\tshows extra info on a file.\n'Run [call number]'\tRuns desired program\n'Exit'\t\tExits program\n""")
    elif CallNum == 'list':
        for num in CallNumDict:
            print(num,f"\t{CallNumDict[num][0]}\n\n")
    else:
        print(CallNumDict[float(CallNum)][1],"\n")

userin = input("Welcome to Program a day!\nTo see commands, type 'help'.\n-> ").lower()

while userin != 'exit':
    print()
    if userin == 'help':
        help(None)
    elif 'help ' in userin:
        userin = userin.split()
        help(userin[1])
    elif 'run' in userin:
        userin = userin.split()
        run(userin(1))
    elif userin == 'list':
        help("list")
    elif 'exit' in userin:
        break
    userin = input('|Base|\n-> ')
print("Goodbye!")
