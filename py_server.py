# -*-coding:utf-8 -*-

from thrift import Thrift
from thrift.Thrift import TException

from PersonServiceImpl import PersonServiceImpl
from py.thrift.genetated import PersonService
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from thrift.server import TServer

try:
    personServiceHandler = PersonServiceImpl()
    processor = PersonService.Processor(personServiceHandler)
    socket = TSocket.TServerSocket(host='127.0.0.1', port=8899)
    transportFactory = TTransport.TFramedTransportFactory()
    protocolFactory = TCompactProtocol.TCompactProtocolFactory()
    server = TServer.TSimpleServer(processor, socket, transportFactory, protocolFactory)
    server.serve()

except TException:
    print("Opps, error")
    raise

