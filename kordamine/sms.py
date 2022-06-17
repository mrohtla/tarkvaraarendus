import requests as r #impordib mooduli
import json as j #impordib mooduli


with open('service.env', 'r') as f:
    service_plan_id = f.read()
with open("token.env", "r") as f:
    access_token = f.read()
from_ = "447520651387"
to_   = "3725585851"

headers = {
    "Authorization":f"Bearer {access_token}",
    "Content-Type":"application/json"
}

payload = {
    "from":from_,
    "to":[to_],
    "body":"Kaupole meeldivad friikad"
}

response = r.post(
    f'https://sms.api.sinch.com/xms/v1/{service_plan_id}/batches',
    headers=headers,
    data=j.dumps(payload)
).json()

print(response)