import requests
import json

web1 = "https://purduediningchatbot.herokuapp.com/webhook"
web2 = "http://127.0.0.1:5000/webhook"
web3 = "http://127.0.0.1:8000/webhook"

r = requests.post(
    web3,
    data=json.dumps(
        {
            "object": "page",
            "entry": [
                {
                    "sender": {"id": "0000"},
                    "recipient": {"id": ""},
                    "timestamp": 1458692752478,
                    "message": {
                        "mid": "mid.1457764197618:41d102a3e1ae206a38",
                        "text": "list all dining halls",
                        "quick_reply": {"payload": "<DEVELOPER_DEFINED_PAYLOAD>"},
                    },
                },
                {
                    "sender": {"id": "0000"},
                    "recipient": {"id": "<PAGE_ID>"},
                    "timestamp": 1458692752478,
                    "message": {
                        "mid": "mid.1457764197618:41d102a3e1ae206a38",
                        "text": "list Wiley meals today",
                        "quick_reply": {"payload": "<DEVELOPER_DEFINED_PAYLOAD>"},
                    },
                },
            ],
        }
    )
)
print(r.text)
