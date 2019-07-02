# Ghasedak-python

Ghasedak sms webservice Python package.

## installation

```shell
pip install ghasedak
```

## usage

Import `ghasedak` package.

```python
import ghasedak

sms = Ghasedak("Your APIKEY")

sms.send({'message':'hello, world!', 'receptor' : '09xxxxxxxxx', 'linenumber': 'xxxx', 'senddate': '', 'checkid': ''})


```

## license

Released under the MIT License.
