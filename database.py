from person import Person
import pickle

import os.path
from os import path

class Database:

    USERS = "users.txt"
    LOGIN = "login.txt"
    def __init__(self):
        self.readPersons()
        self.readUsers()

    def userNames(self):
        ret = []
        for (user, p) in self.users:
            ret.append(user)
        return ret

    def isUserPassValid(self, username,password):
        return (username,password) in self.users

    def getUsers(self):
        return self.persons.keys()

    def getPersons(self):
        return list(self.persons.values())

    def readUser(self,username):
        return self.persons[username]

    def removeUser(self,username):
        self.persons.pop(username, None)

    def readUsers(self):
        if (not path.exists(self.LOGIN)):
            self.users = []
        else:
            with open(self.LOGIN, 'rb') as input:
                self.users = pickle.load(input)

    def readPersons(self):
        if (not path.exists(self.USERS)):
            self.persons = {}
        else:
            with open(self.USERS, 'rb') as input:
                self.persons = pickle.load(input)

    def addUser(self, user, password):
        if(user not in self.persons):
            self.users.append((user,password))
        else:
            print("Person already exists")

    def addPerson(self, user, person):
        if(user not in self.persons):
            self.persons[user] = person
        else:
            print("Person already exists")

    def closeData(self):
        self.writeUsers()
        self.writePersons()

    def writePersons(self):
        with open(self.USERS, 'wb') as output:
            pickle.dump(self.persons, output, pickle.HIGHEST_PROTOCOL)

    def writeUsers(self):
        with open(self.LOGIN, 'wb') as output:
            pickle.dump(self.users, output, pickle.HIGHEST_PROTOCOL)