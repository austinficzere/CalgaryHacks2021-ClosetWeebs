from person import Person
from database import Database

def createAccount(server):
    user = input("Enter your username: ")
    # compare with database
    pasW = input("Enter your password: ")

    server.addUser(user, pasW)

    #year, concentration, major
    name = input("Enter your full name: ")
    year = int(input("Enter your year at the university: "))
    major = input("Enter your major at the university: ")
    conce = input("Enter your concentration in CPSC: ")

    #classes, interests
    classArr = []
    classI = int(input("Enter a class you are in, or -1 if you have entered all classes already: "))

    while (classI != -1):
        classArr.append(classI)
        classI = int(input("Enter a class you are in, or -1 if you have entered all classes already: "))


    print("""Enter the number corresponding to the interest that you identify with\n 
           0 Sports\n
           1 Gaming\n
           2 Reading\n
           3 Coding\n
           4 Music\n
           4 Stocks\n
           5 Movies\n
           6 Done Selecting Interests\n""")
    
    i = int(input())
    interestsArr = []

    while (i != 6):
        interestsArr.append(i)
        i = int(input())

    descr = input("Enter the bio you want others to see: ")

    prior = int(input("Enter the priority by which you want to be matched: 1 -> Year 2 -> Major 3 -> Concentration 4 -> Classes 5 -> Interests"))

    return user, name, year, major, conce, classArr, interestsArr, descr, prior


def login(server):
    user = input("Enter your username: ")
    pasW = input("Enter your password: ")

    test = False
    while (server.isUserPassValid(user, pasW) == test):
        print("Invalid Username or Password\n")
        user = input("Enter your username or enter nothing exit: ")
        if (user == ""):
            break
        pasW = input("Enter your password: ")



def main():
    server = Database()
    userChoice = int(input("Enter 1 to Create Account or Enter 2 to Login with an existing account: "))

    if userChoice == 1:
        username, name, userYear, userMajor, userConcen, userClassArr, userInterestArr, userDesc, userPrior = createAccount(server) #after they create account, they will be logged in

        user = Person(name, userYear, userMajor, userConcen, userClassArr, userInterestArr, userDesc, userPrior)
        server.addPerson(username, user)

    elif userChoice == 2:
        login(server) #all information is saved 
    else:
        print("Invalid option selected")
        exit(1)

    for person in server.getPersons():
        person.toString()
        print()

    server.closeData()

main()
