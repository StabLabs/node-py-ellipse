from comtypes.client import CreateObject, PumpEvents, GetEvents
import time
import sys


class E3EventSink(object):

    def __init__(self):
        super(E3EventSink, self).__init__()

    def _IE3DataAccessManagerEvents_OnValueChanged(self, this, pathname, timestamp, quality, value):
        print("{} {} {} {}".format(time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime()), quality, pathname, value))


class PyE3DataAccess(object):

    def __init__(self, server='localhost'):
        super(PyE3DataAccess, self).__init__()
        self._engine = CreateObject("{80327130-FFDB-4506-B160-B9F8DB32DFB2}")
        self._engine.Server = server
        self._sinkEvents = E3EventSink()
        self._showEvents = GetEvents(source=self._engine, sink=self._sinkEvents)
    
    def batchRegisterCallback(self, path=['']):
    	return self._engine.BatchRegisterCallback(path)

    def batchUnregisterCallback(self, path=['']):
    	return self._engine.BatchUnregisterCallback(path)

    def registerCallback(self, path):
        return self._engine.RegisterCallback(path)

    def unregisterCallback(self, path):
        return self._engine.UnregisterCallback(path)

    def clearCallbacks(self):
    	return self._engine.ClearCallbacks()
        
    def updateServer(self, server):
        self._engine.Server = server
        return self._engine.Server

    def disconnect(self):
        return self._engine.Disconnect()

    def connect(self):
        return self._engine.Connect()

    def getDomainState(self):
        return self._engine.DomainState

    def readvalue(self, pathname):
        return self._engine.ReadValue(pathname)

    def executeQuery(self, pathname, Names=[''], Values=['']):
        return self._engine.ExecuteQuery(pathname, Names, Values)

    def writevalue(self, pathname, date, quality, value):
        return self._engine.WriteValue(pathname, date, quality, value)

    def closeConnect(self):
        del self._engine

    def pumpEventsChanged(self, time=-1):
    	return PumpEvents(time)
if __name__ == '__main__':
	pyE3DataAccess = PyE3DataAccess(server="localhost")
	print(pyE3DataAccess.readvalue(pathname=sys.argv[1] + ".Value"))
    ##print(pyE3DataAccess.readvalue(pathname="Dados." + sys.argv[1] + ".Value"))