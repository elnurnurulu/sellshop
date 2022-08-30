import json
from core.config import RedisConfig
from core.send_mail import SendMail


class Handler(RedisConfig):
    
    def __init__(self):
        p = self.client.pubsub()
        p.subscribe(**{self.CHANNEL_NAME: self.send_mail})
        p.run_in_thread()
    
    def send_mail(self, message_data):
        print(message_data)
        message = self.to_dict(message_data['data'])
        if message.get('event_type') == "send_mail":
            print('message', message)
            data = message.pop('data')
            SendMail(data=data)
            print('sent')
            

    def to_dict(self,message_data):
        return json.loads(message_data)