import requests
from sample import sample

r = requests.post(#Your API,
                  json={"inputTranscript": sample})
print(r.status_code, r.reason)
print(r.json())
