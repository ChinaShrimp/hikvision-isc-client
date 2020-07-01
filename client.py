import json
from api import post

class HikVisionClient(object):
  def __init__(self, app_key, app_secret, ip, port, https=True):
    self.app_key = app_key
    self.app_secret = app_secret
    self.ip = ip
    self.port = port
    self.https = https

  def get_cameras(self, body):
    result = post(self.app_key, 
      self.app_secret, 
      "/artemis/api/resource/v1/cameras", 
      "POST", 
      self.ip,
      self.port,
      body,
      self.https)

    result = json.loads(result)

    if result["code"] != '0':
      return []

    return result['data']['list']

  def get_regions(self, body):
    result = post(self.app_key, 
      self.app_secret, 
      "/artemis/api/resource/v1/regions", 
      "POST", 
      self.ip,
      self.port,
      body,
      self.https)

    result = json.loads(result)

    if result["code"] != '0':
      return []

    return result['data']['list']

  def get_camera_preview_url(self, camera_index, stream_type, protocol, trans_mode, expand):
    result = post(self.app_key, 
      self.app_secret, 
      "/artemis/api/video/v1/cameras/previewURLs", 
      "POST", 
      self.ip,
      self.port,
      {
        "cameraIndexCode": camera_index,
        "streamType": stream_type,
        "protocol": protocol,
        "transmode": trans_mode,
        "expand": expand
      },
      self.https)

    result = json.loads(result)

    if result["code"] != '0':
      return ''

    return result['data']['url']