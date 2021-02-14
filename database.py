from person import Person
import pickle

import os.path
from os import path

class Database:

    USERS = "users.txt"
    LOGIN = "login.txt"
    CHAT = "chat.txt"

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

    def getChat(self,user,other):
        return self.chat[(user,other)]

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

    def readChat(self):
        if (not path.exists(self.CHAT)):
            self.chat = {}
        else:
            with open(self.CHAT, 'rb') as input:
                self.chat = pickle.load(input)

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

    def addChat(self, user, other, exchange):
        self.chat[(user,other)].append(exchange)
        self.chat[(other,user)].append(exchange)

    def addPerson(self, user, person):
        if(user not in self.persons):
            self.persons[user] = person
        else:
            print("Person already exists")

    def closeData(self):
        self.writeUsers()
        self.writePersons()
        self.writeChat()

    def writePersons(self):
        with open(self.USERS, 'wb') as output:
            pickle.dump(self.persons, output, pickle.HIGHEST_PROTOCOL)

    def writeUsers(self):
        with open(self.LOGIN, 'wb') as output:
            pickle.dump(self.users, output, pickle.HIGHEST_PROTOCOL)

    def writeChat(self):
        with open(self.CHAT, 'wb') as output:
            pickle.dump(self.chat, output, pickle.HIGHEST_PROTOCOL)
    