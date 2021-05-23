import json
from channels.generic.websocket import WebsocketConsumer

class RuncommandConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        command = text_data_json['command']


        self.send(text_data=json.dumps({
            'result': commadn
        }))
