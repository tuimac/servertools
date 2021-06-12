import json
import logging
import traceback
import socket
import subprocess
from multiprocessing import cpu_count

logger = logging.getLogger("django")

class Runshell:
    @staticmethod
    def run(request):
        try:
            logger.error(request)
        except:
            logger.error(traceback.format_exc())
