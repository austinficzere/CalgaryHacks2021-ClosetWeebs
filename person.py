class Person:
    def __init__(self, name, year, major, concentrations, classes, interests, description, priority):
        self.name = name #String
        self.year = year #Int
        self.major = major # String
        self.concentrations = concentrations # String
        self.classes = classes #[String]
        self.interests = interests #[String]
        self.description = description #String
        self.priority = priority #int

    def getYear(self):
        return self.year

    def getName(self):
        return self.name

    def getMajor(self):
        return self.major
    
    def getConcen(self):
        return self.concentrations

    def getClasses(self):
        return self.classes
    
    def getInterests(self):
        return self.interests

    def getDescription(self):
        return self.description

    def getPriority(self):
        return self.priority

    def setInterests(self,inter):
        self.interests = inter

    def setName(self,name):
        self.name = name

    def setMajor(self, major):
        self.major = major
    
    def setConcen(self,concen):
        self.concentrations = concen

    def setClasses(self,classes):
        self.classes = classes
    
    def setYear(self,year):
        self.year = year

    def editDescription(self, description):
        self.description = description

    def setPriority(self, pri):
        self.priority = pri
        
    def toString(self):
        print("Name: ", getName())
        print("Year of Study: ", getYear())
        print("Major: ", getMajor())
        print("Concentration: ", getConcen())
        print("Classes: ", getClasses())
        print("Interests: ", getInterests())
        print("Priority: ", getPriority())
        print("Description: ", getDescription())

