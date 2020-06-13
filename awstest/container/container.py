import json
import logging
import traceback
import socket
from multiprocessing import cpu_count

logger = logging.getLogger("django")

class Container:
    def __init__(self):
        self.response = dict()

    def query(self) -> dict:
        try:
            self.response["IPAddress"] = socket.gethostbyname(socket.gethostname())
            self.response["Hostname"] = socket.gethostname()
            self.response["CPU cores"] = cpu_count()
            #print(self.response)
            return self.response
        except json.decoder.JSONDecodeError as e:
            self.response[target] = body
            logger.error("".join(traceback.format_list()))
            return self.response
        except KeyError as e:
            self.response["Error"] = "Query Error(EC2)"
            logger.error("".join(traceback.format_list()))
            return self.response
        except:
            traceback.print_exc()
            self.response["Error"] = "General Exception of Error(EC2)"
            logger.error("".join(traceback.format_list()))
            return self.response
