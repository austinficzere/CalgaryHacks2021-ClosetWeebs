from person import Person

def createAccount():
    user = input("Enter your username: ")
    # compare with database
    pasW = input("Enter your password: ")

    #year, concentration, major
    name = input("Enter your full name: ")
    year = int(input("Enter your year at the university: "))
    major = input("Enter your major at the university: ")
    conce = input("Enter your concentration in CPSC: ")

    #classes, interests
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


    return name, year, major, conce, interestsArr


def login():
    user = input("Enter your username: ")
    # compare with database to make sure it exists
    pasW = input("Enter your password: ")
    # check if password is valid



def main():
    userChoice = input("Enter 1 to Create Account or Enter 2 to Login with an existing account: ")

    if userChoice == 1:
        name, userYear, userMajor, userConcen, userInterestArr = createAccount() #after they create account, they will be logged in
    elif userChoice == 2:
        login() #all information is saved 
    else 
        print("Invalid option selected")

    user = Person()

    user.setName(name)
    user.setYear(userYear)
    user.setMajor(userMajor)
    user.setConcen(userConcen)


