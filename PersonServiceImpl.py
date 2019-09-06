# -*- coding:utf-8 -*-

from py.thrift.genetated import ttypes


class PersonServiceImpl:
    def getPersonByUsername(self, username):
        print("got java client param" + username)
        person = ttypes.Person()
        person.username = username
        person.age = 20
        person.married = False
        return person

    def savePerson(self, person):
        print("got java client param")

        print(person.username)
        print(person.age)
        print(person.married)
