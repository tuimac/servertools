import json
import logging
import traceback
import socket
from multiprocessing import cpu_count

logger = logging.getLogger("django")

class Host:
    def __init__(self):
        self.response = dict()

    def query(self) -> dict:
        try:
            self.response["IPAddress"] = socket.gethostbyname(socket.gethostname())
            self.response["Hostname"] = socket.gethostname()
            self.response["CPU_cores"] = cpu_count()
            return self.response
        except:
            self.response["Traceback"] = traceback.format_exc().splitlines()[-1]
            self.response["Messages"] = "This error is out of scope."
            logger.error(traceback.format_exc())
            return self.response
