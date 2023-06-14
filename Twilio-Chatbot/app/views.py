#all the routes for my website go here

#import relevant modules
import os
from app import app
from flask import render_template, flash,redirect,request, make_response,json,url_for,jsonify
from flask_login import LoginManager,login_required,logout_user,login_user,current_user
from flask_mail import Mail, Message
from .forms import ChatForm
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import openai
openai.api_key = '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'
client = Client('AC4c6fdc6900c4f4f80963e7d13f988fdb', '034b486b919fd11734d3766942247611')

#it is a sample view to test a sample JSON File with flask. as i am not very familiar with JSON i am trying an example

@app.route('/', methods=['GET','POST'])
def load_all():
    form = ChatForm()
    if form.validate_on_submit():
        user_message = form.fname.data

        # Call your chatbot function to generate a response
        bot_response = generate_chatbot_response(user_message)

        # Send the bot response as an SMS using Twilio
        send_sms(bot_response,form.pno.data)
    #loads the first and last name from the json file
    #embeds the data into a template
    return render_template('homepage.html',form = form)

def generate_chatbot_response(user_message):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_message,
        max_tokens=60
    )
    bot_response = response.choices[0].text.strip()
    return bot_response

class ChatMessage:
    def __init__(self, user_message, bot_response):
        self.user_message = user_message
        self.bot_response = bot_response


def send_sms(message,number):
    # Use Twilio to send an SMS message
    account_sid = 'AC4c6fdc6900c4f4f80963e7d13f988fdb'
    auth_token = '034b486b919fd11734d3766942247611'
    twilio_number = '+447360269493'
    recipient_number = number

    client = Client(account_sid, auth_token)
    client.messages.create(
        body=message,
        from_=twilio_number,
        to=recipient_number
    )

# @app.route('/delivery-status', methods=['POST'])
# def handle_delivery_status():
#     # Parse the delivery status update from the Twilio webhook
#     delivery_status = request.form.get('MessageStatus')
#     message_sid = request.form.get('MessageSid')

#     # Handle the delivery status update as per your requirements
#     # You can update your chat message status, log the status, etc.

#     return 'OK'  # Return a response to acknowledge the delivery status update
