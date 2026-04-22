from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
MY_PHONE = os.getenv("MY_PHONE")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_sms(self, message):
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        
        message = client.messages.create(
            body = message,
            from_ = TWILIO_NUMBER,
            to = MY_PHONE,
        )
        
        print("Message Sent :", message.sid)