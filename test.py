import requests
import json



r = requests.post(
    "https://purduediningchatbot.herokuapp.com/webhook_dev",
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
