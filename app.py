from flask import Flask, jsonify, request
import json
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

@app.route("/")
def hello():
    return jsonify({"key": 1234, "typed": " 12734901"})


@app.route("/webhook", methods=["POST"])
def get():
    content = request.data
    data = json.loads(content)
    entries = data["entry"]
    retmes = ""
    if data["object"] == "page":
        for entry in entries:
            mes = entry["message"]["text"]
            loc = getLoc(mes)
            if loc == "all":
                for l in locations:
                    retmes += l + "\n"
            elif loc == "none":
                retmes += "none\n"
            else:
                retmes += loc + '\n'
            
    return sendMes(retmes)

def sendMes(message):
    return json.dumps({"messaging_type": "RESPONSE", "recipient": {"id": psid},"message": {"text": message}}, indent=3)

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