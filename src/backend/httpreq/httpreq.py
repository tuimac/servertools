import urllib.request
import json
import logging
import traceback

logger = logging.getLogger("django")

class Httpreq:
    def __init__(self, header, body):
        self.response = dict()
        self.header = header
        self.body = body

    def query(self) -> dict:
        try:
            self.response['header'] = self.header
            self.response['body'] = self.body
            return self.response
        except:
            self.response["Traceback"] = traceback.format_exc().splitlines()[-1]
            self.response["Messages"] = "This error is out of scope."
            logger.error(traceback.format_exc())
            return self.response
