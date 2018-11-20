from flask import Flask, jsonify, request, Response
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
    data = json.loads(content)
    entries = data["entry"]
    retmes = ""
    if data["object"] == "page":
        for entry in entries:
            user_id = entry['messaging'][0]['sender']['id']
            mes = entry["message"]["text"]
            loc = getLoc(mes)
            if loc == "all":
                for l in locations:
                    retmes += l + " "
            elif loc == "none":
                retmes += "none"
            else:
                retmes += loc + ' '
            send = sendMes(retmes,user_id)
            requests.post('https://graph.facebook.com/v2.6/me/messages?access_token=' + access_token, data=send)
    return Response(response="EVENT RECEIVED",status=200)

@app.route("/webhook_dev", methods=["POST"])
def getdev():
    content = request.data
    data = json.loads(content)
    entries = data["entry"]
    retmes = ""
    if data["object"] == "page":
        for entry in entries:
            user_id = entry['messaging'][0]['sender']['id']
            mes = entry["message"]["text"]
            loc = getLoc(mes)
            if loc == "all":
                for l in locations:
                    retmes += l + " "
            elif loc == "none":
                retmes += "none"
            else:
                retmes += loc + ' '
            send = sendMes(retmes,user_id)
            
    return send

def sendMes(message,userid):
    return json.dumps({"recipient": {"id": userid},"message": {"text": message}},)

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
    app.run(debug=True, host = '0.0.0.0')