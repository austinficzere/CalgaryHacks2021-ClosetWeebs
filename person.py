class Person:
    def __init__(self, name, year, major, concentrations, classes, interests, description):
        self.name = name #String
        self.year = year #Int
        self.major = major # String
        self.concentrations = concentrations # String
        self.classes = classes #[Strings]
        self.interests = interests #[(Int,String)]
        self.description = description #String

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
    
    def getInterets(self):
        return self.interests
    
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
        
