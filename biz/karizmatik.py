import os
import requests
from dotenv import load_dotenv


def configure():
    load_dotenv()
    
configure()

def send_messages():
    url = 'https://www.fast2sms.com/dev/bulkV2'
    message = "This is Karizmatik shoe Cleaning Service, we are grateful for your patronage. We re-routed our website to https://karizmatikshoes.vercel.app to serve you better. Let's make our shoes shine again. Thank you."
    payload = {
        'sender_id': 'TXTIND',
        'message': message,
        'route': 'q', 
        'language': 'english',
        'numbers': 8054108169
    }
    
    headers = {
        'authorization': os.getenv('FAST2SMS_API'),
        'Content-Type':'application/x-www-form-urlencoded'
    }
    #print(f"API KEY: {os.getenv('FAST2SMS_API')}")
    response = requests.post(url, data=payload, headers=headers)
    
    return response.text

print(send_messages())