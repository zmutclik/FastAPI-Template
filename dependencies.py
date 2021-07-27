import hashlib
import base64
import hmac
from . import config
from datetime import datetime


def tokenheaders():
    time_now = datetime.utcnow()
    time_last = datetime.strptime(
        "1970-01-01 00:00:00", '%Y-%m-%d %H:%M:%S')
    Timestamp = str(int(time_now.strftime("%s")) -
                    int(time_last.strftime("%s")))
    signature = hmac.new(bytes(config.apikeysecret, 'latin-1'),
                         msg=bytes(config.apikeydata+"&"+Timestamp, 'latin-1'), digestmod=hashlib.sha256)
    return {
        'Accept': 'application/json',
        'X-Cons-ID': config.apikeydata,
        'X-Timestamp': Timestamp,
        'X-Signature': base64.b64encode(signature.digest()).decode(),
    }
