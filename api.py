import requests
import json

from sign import sign

def post(app_key, app_secret, uri, method, ip, port, body, https=True):
  url = "https://" if https else "http://"
  url += ip + ":" + port + uri 

  headers = sign(app_key, app_secret, body, uri, method)
  
  r = requests.post(url, headers=headers, data=json.dumps(body), verify=False)

  return r.content
