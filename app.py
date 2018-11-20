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
from flask import Flask, request, Response
import requests, json, random, os
app = Flask(__name__)

# env_variables
# token to verify that this bot is legit
verify_token = os.getenv('VERIFY_TOKEN', None)
# token to send messages through facebook messenger
access_token = os.getenv('ACCESS_TOKEN', None)

@app.route('/webhook', methods=['GET'])
def webhook_verify():
    if request.args.get('hub.verify_token') == verify_token:
        return request.args.get('hub.challenge')
    return "Wrong verify token"

@app.route('/webhook', methods=['POST'])
def webhook_action():
    data = json.loads(request.data.decode('utf-8'))
    for entry in data['entry']:
        user_message = entry['messaging'][0]['message']['text']
        user_id = entry['messaging'][0]['sender']['id']
        response = {
            'messaging_type': 'MESSAGE_TAG',
            'recipient': {'id': user_id},
            'message': {}
        }
        response['message']['text'] = handle_message(user_id, user_message)
        r = requests.post(
            'https://graph.facebook.com/v2.6/me/messages/?access_token=' + access_token, json=response)
    return Response(response="EVENT RECEIVED",status=200)


def handle_message(user_id, user_message):
    # DO SOMETHING with the user_message ... ¯\_(ツ)_/¯
    return "Hello "+user_id+" ! You just sent me : " + user_message

@app.route('/privacy', methods=['GET'])
def privacy():
    # needed route if you need to make your bot public
    return "This facebook messenger bot's only purpose is to [...]. That's all. We don't use it in any other way."

@app.route('/', methods=['GET'])
def index():
    return "Hello there, I'm a facebook messenger bot."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')