# Ghasedak-python

[Ghasedak sms webservice](https://ghasedak.io) python package.

## installation

You can simply install ghasedak python package with `pip`:

```shell
pip install ghasedak
```

## usage


```python
import ghasedak

sms = ghasedak.Ghasedak("Your APIKEY")

sms.send({'message':'hello, world!', 'receptor' : '09xxxxxxxxx', 'linenumber': 'xxxx', 'senddate': '', 'checkid': ''})

```

## license

Released under the MIT License.
