"""from flask import Flask, jsonify, request, Response
import json
import os
import requests
import datetime
import xml.etree.ElementTree as ET
app = Flask(__name__)
url = "https://api.hfs.purdue.edu/menus/v2/locations/"
locations = ["Wiley", "Ford", "Hillenbrand", "The Gathering Place", "Earhart", "Windsor"]
info = ["Meal", "Hours"]
tempt = datetime.datetime.now()
time = tempt.strftime("%m-%d-%Y")
psid = 1212
access_token = os.getenv("ACCESS_TOKEN")

@app.route("/")
def hello():
    return jsonify({"key": 1234, "typed": " 12734901"})

# env_variables
# token to verify that this bot is legit
verify_token = os.getenv("VERIFY_TOKEN")
# token to send messages through facebook messenger


@app.route('/webhook', methods=['GET'])
def webhook_verify():
    if request.args.get('hub.verify_token') == verify_token:
        return request.args.get('hub.challenge')
    return "Wrong verify token"

@app.route("/webhook", methods=["POST"])
def get():
    content = request.data
    f = open("temp.txt","a")
    data = json.loads(content)
    f.write(json.dumps(data))
    f.close()
    entries = data["entry"]
    retmes = ""
    if data["object"] == "page":
        for entry in entries:
            user_mes = entry['messaging'][0]['message']['text']
            user_id = entry['messaging'][0]['sender']['id']
            loc = getLoc(user_mes)
            if loc == "all":
                for l in locations:
                    retmes += l + " "
            elif loc == "none":
                retmes += "none"
            else:
                retmes += loc + ' '
            send = sendMes(retmes,user_id)
            requests.post('https://graph.facebook.com/v2.6/me/messages?access_token=' + access_token, json=send)
    return Response(response="EVENT RECEIVED",status=200)


def sendMes(message,userid):
    return {"recipient": {"id": userid},"message": {"text": message}}

def getLoc(message):
    split_string = message.split(" ")
    if message == "list all dining halls":
        return "all"
    elif split_string[3] == "today":
        strn = split_string[1]
        
        for loc in locations:
            if loc == strn:
                return strn
        return "none"
    return "none"

if __name__=='main':
    app.run(debug=True, host = '0.0.0.0')"""
import random
from flask import Flask, request
from pymessenger.bot import Bot
import os

app = Flask(__name__)
ACCESS_TOKEN = getenv("ACCESS_TOKEN")
VERIFY_TOKEN = getenv('VERIFY_TOKEN')
bot = Bot(ACCESS_TOKEN)

#We will receive messages that Facebook sends our bot at this endpoint 
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook.""" 
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    #if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
       output = request.get_json()
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                #Facebook Messenger ID for user so we know where to send response back to
                recipient_id = message['sender']['id']
                if message['message'].get('text'):
                    response_sent_text = get_message()
                    send_message(recipient_id, response_sent_text)
                #if user sends us a GIF, photo,video, or any other non-text item
                if message['message'].get('attachments'):
                    response_sent_nontext = get_message()
                    send_message(recipient_id, response_sent_nontext)
    return "Message Processed"


def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


#chooses a random message to send to the user
def get_message():
    sample_responses = ["You are stunning!", "We're proud of you.", "Keep on being you!", "We're greatful to know you :)"]
    # return selected item to the user
    return random.choice(sample_responses)

#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

if __name__ == "__main__":
    app.run(debug=True)