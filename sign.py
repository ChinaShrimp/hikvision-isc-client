from email.utils import formatdate
from datetime import datetime
from time import mktime
import json
import hashlib
import hmac
import base64

def sign(app_key, app_secret, body, uri, method):
  print(json.dumps(body))
  content_md5 = hashlib.md5()
  content_md5.update(json.dumps(body).encode('utf-8'))
  content_md5_str = str(base64.b64encode(content_md5.digest()), "utf-8")
  now = datetime.now()
  stamp = mktime(now.timetuple())
  date = formatdate(
      timeval     = stamp,
      localtime   = False,
      usegmt      = True
  )

  string_to_be_signed = method + "\n"                 \
                        + "*/*" + "\n"                \
                        + "application/json" + "\n"   \
                        + date + "\n"                 \
                        + "x-ca-key:" + app_key + "\n" \
                        + uri

  signature = str(base64.b64encode(hmac.new(
    app_secret.encode("utf-8"),
    string_to_be_signed.encode("utf-8"),
    digestmod=hashlib.sha256
  ).digest()), "utf-8")

  return {
    "Accept": "*/*",
    "Content-Type": "application/json",
    "Date": date,
    "X-Ca-Key": app_key,
    "X-Ca-Signature": signature,
    "X-Ca-Signature-Headers": "X-Ca-Key"
  }