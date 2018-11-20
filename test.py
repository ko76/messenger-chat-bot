import requests
import json



r = requests.post(
    "http://localhost:5000/webhook",
    data=json.dumps(
        {
            "object": "page",
            "entry": [
                {
                    "sender": {"id": "<PSID>"},
                    "recipient": {"id": "<PAGE_ID>"},
                    "timestamp": 1458692752478,
                    "message": {
                        "mid": "mid.1457764197618:41d102a3e1ae206a38",
                        "text": "list all dining halls",
                        "quick_reply": {"payload": "<DEVELOPER_DEFINED_PAYLOAD>"},
                    },
                },
                {
                    "sender": {"id": "<PSID>"},
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
