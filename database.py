from person import Person
import pickle

import os.path
from os import path

class Database:

    USERS = "users.txt"
    def __init__(self):
        self.readPersons()

    def getPersons(self):
        return self.persons

    def readPersons(self):
        if (not path.exists(self.USERS)):
            self.persons = []
        else:
            with open(self.USERS, 'rb') as input:
                self.persons = pickle.load(input)

    def addPerson(self,person):
        self.persons.append(person)

    def closeData(self):
        self.writePersons()

    def writePersons(self):
        with open(self.USERS, 'wb') as output:
            pickle.dump(self.persons, output, pickle.HIGHEST_PROTOCOL)
         