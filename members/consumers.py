import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            'chat',
            self.channel_name
        )
        self.accept()
 
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            'chat',
            self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']


        async_to_sync(self.channel_layer.group_send)(
            'chat',
            {
                'type': 'chat.message',
                'message': message
                }
                )

    def chat_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'message': message
        }))
