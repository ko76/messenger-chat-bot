import requests
import json

web1 = "https://purduediningchatbot.herokuapp.com/webhook"
web2 = "http://127.0.0.1:5000/webhook"
web3 = "http://127.0.0.1:8000/webhook"

r = requests.post(
    web3,
    data=json.dumps(
        {
            "object":"page",
            "entry":[
                {
                    "messaging":[
                        {
                            "message":{
                                "text":"list all dining halls",
                                "seq":20,
                                "mid":"mid.1466015596912:7348aba4de4cfddf91"
                            },
                            "timestamp":1466015596919,
                            "sender":{
                                "id":"885721401551027"
                            },
                            "recipient":{
                                "id":"260317677677806"
                            }
                        }
                    ],
                    "time":1466015596947,
                    "id":"260317677677806"
                }
            ]
        }
    )
)
print(r.text)
