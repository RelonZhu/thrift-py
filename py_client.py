# -*- coding:utf-8 -*-


from thrift import Thrift
from thrift.Thrift import TException
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol

from py.thrift.genetated import PersonService, ttypes

try:
    tSocket = TSocket.TSocket('localhost', 8899)
    tSocket.setTimeout(600)

    transport = TTransport.TFramedTransport(tSocket)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = PersonService.Client(protocol)

    transport.open()

    person = client.getPersonByUsername("张三")
    print(person.username)
    print(person.age)
    print(person.married)

    print('-------------------------------------')
    new_person = ttypes.Person()
    new_person.username = '李四'
    new_person.age = 30
    new_person.married = True
    client.savePerson(new_person)

    transport.close()

except TException:
    print('opps, error')
    raise


