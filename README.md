# HIKVISION iSC Python SDK

This is the Python SDK to interact with Hikvision iSC platform using Hikvision's open API.

## Usage

```python
from hikvision-isc-client.client import HikVisionClient

client = HikVisionClient("AK",
        "SK",
        "IP",
        "PORT")

result = client.get_cameras({
        "pageSize": 100,
        "pageNo": 1
      })


result = client.get_regions({
        "pageSize": 100,
        "pageNo": 1
      })

result = client.get_camera_preview_url("camera index id", 0, "rtsp", 1, "streamform=rtp")
```

or you could use `post` method from api:

```python
import hikvision-isc-client.api

post(app_key, app_secret, uri, method, ip, port, body, https=True)
```
