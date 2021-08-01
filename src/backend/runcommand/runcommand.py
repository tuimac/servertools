import json
from channels.generic.websocket import WebsocketConsumer
import logging
import traceback
import subprocess
import os

logger = logging.getLogger("django")

class Runcommand:
    @staticmethod
    def run(command):
        if 'cd ' in command or 'cd' == command:
            if command == 'cd':
                path = '~'
                path = os.path.expanduser(path)
                os.chdir(path)
            else:
                path = command.split()[1]
                os.chdir(path)
            return ''
        else:
            process = subprocess.Popen(
                ['bash'],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            out, err = process.communicate(input=command.encode())
            if out:
                return out.decode()
            elif err:
                return err.decode()
            else:
                return False

class RuncommandConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass       

    def receive(self, text_data):
        try:
            data = json.loads(text_data)
            command = data['command']
            result = Runcommand.run(command)
            logger.error(result)
            self.send(text_data=json.dumps({
                'result': result
            }))
        except:
            logger.error(traceback.format_exc())
