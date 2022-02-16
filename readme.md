# Ghasedak-python

[Ghasedak sms webservice](https://ghasedak.me) python package.

## installation

You can simply install ghasedak python package with `pip`:

```shell
pip install ghasedakpack
```

## usage


```python
import ghasedakpack

#create an instance:
sms = ghasedakpack.Ghasedak("Your APIKEY")

#send a single message to a single number:
sms.send({'message':'hello, world!', 'receptor' : '09xxxxxxxxx', 'linenumber': 'xxxx', 'senddate': '', 'checkid': ''})

#send a single message to multiple numbers:
sms.bulk1({'message':'hello, world!', 'receptor' : '09xxxxxxxxx,09xxxxxxxxx,09xxxxxxxxx', 'linenumber': 'xxxx', 'senddate': '', 'checkid': ''})

#send multiple massages to multiple numbers:
sms.bulk2({'message':'hello, world!,another massage', 'receptor' : '09xxxxxxxxx,09xxxxxxxxx,09xxxxxxxxx', 'linenumber': 'xxxx', 'senddate': '', 'checkid': ''})

#get the status of massages:
print(sms.status({'id': 'messageId', 'type': '1'}))

#send verification massages:
sms.verification({'receptor': '09xxxxxxxxx','type': '1','template': 'Your Template','param1': '','param2': '','param3': ''})
```

## license

Released under the MIT License.
