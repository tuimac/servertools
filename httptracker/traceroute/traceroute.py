import socket
import traceback
import logging
import random
import time
from queue import Queue
from threading import Thread

logger = logging.getLogger("django")

class Traceroute:
    def __init__(self, destIp):
        self.sourceIp = socket.gethostbyname(socket.gethostname())
        self.destIp = destIp
        self.ttl = 30
        self.response = dict()
        self.__run()

    def __run(self):
        try:
            self.inbound = Inbound(self.sourceIp)
            self.inbound.daemon = True
            self.inbound.start()
            self.outbound = Outbound(self.destIp)
            self.outbound.daemon = True
            self.outbound.start()
        except:
            self.response["traceback"] = traceback.format_exc().splitlines()[-1]
            self.response["messages"] = "this error is out of scope."
            logger.error(traceback.format_exc())
            return self.response

    def traceroute(self):
        try:
            outbound = self.outbound.getOutboundQueue()
            inbound = self.inbound.getInboundQueue()
            for ttl in range(1, self.ttl + 1):
                outbound.put(((b""), ttl))
                message, info = inbound.get()
                print(info)
            self.outbound.closeEndpoint()
            self.inbound.closeEndpoint()
        except:
            self.response["traceback"] = traceback.format_exc().splitlines()[-1]
            self.response["messages"] = "this error is out of scope."
            logger.error(traceback.format_exc())
            return self.response

class Inbound(Thread):
    def __init__(self, ip):
        Thread.__init__(self)
        self.__queue = Queue()
        self.__ip = ip
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        self.__delete = False
        self.__buffer = 0xffff

    def run(self):
        try:
            while not self.__delete:
                data = self.__socket.recvfrom(self.__buffer)
                self.__queue.put(data)
        except KeyboardInterrupt:
            self.closeEndpoint()
        except Exception as e:
            raise e

    def getInboundQueue(self):
        return self.__queue

    def closeEndpoint(self):
        try:
            self.__delete = True
            self.__queue.put((b"", ("0.0.0.0", 0)))
            self.__socket.close()
        except Exception as e:
            raise e

class Outbound(Thread):
    def __init__(self, ip):
        Thread.__init__(self)
        self.__queue = Queue()
        self.__ip = ip
        self.__port = random.randint(33434, 33534)
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.__delete = False

    def run(self):
        try:
            while not self.__delete:
                message, ttl = self.__queue.get()
                self.__socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
                self.__socket.sendto(message, (self.__ip, self.__port))
        except KeyboardInterrupt:
            self.closeEndpoint()
        except Exception as e:
            raise e

    def getOutboundQueue(self):
        return self.__queue

    def closeEndpoint(self):
        try:
            self.__delete = True
            self.__queue.put((b"", ("0.0.0.0", 0)))
            self.__socket.close()
        except Exception as e:
            raise e
