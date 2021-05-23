import json
from channels.generic.websocket import WebsocketConsumer
from queue import Queue
from threading import Thread
import logging
import traceback
import subprocess

logger = logging.getLogger("django")

class Runcommand(Thread):
    def __init__(self, queue, command):
        Thread.__init__(self)
        self.queue = queue
        self.command = command

    def run(self):
        try:
            process = subprocess.Popen(self.command.split(), stdout=subprocess.PIPE)
            while True:
                output = process.stdout.readline()
                if output:
                    self.queue.put(output.strip().decode())
                else:
                    self.queue.put(0xff)
                    logger.error('hello')
                    break
        except:
            logger.error(traceback.format_exc())

class RuncommandConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            command = text_data_json['command']
            queue = Queue()
            runcommand = Runcommand(queue, command)
            runcommand.start()
            while True:
                result = queue.get()
                if result == 0xff: break
                self.send(text_data=json.dumps({
                    'result': result
                }))
            runcommand.join()
        except:
            logger.error(traceback.format_exc())
