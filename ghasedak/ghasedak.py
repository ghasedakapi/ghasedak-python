# -*- coding: utf-8 -*-
"""
	ghasedak.py
	~~~~~~~~~
	:copyright: (c) 2019 by Ghasedak ICT
	:license: MIT, see LICENSE for more details.
"""
import requests
import json


class Ghasedak:
    """docstring for Ghasedak."""

    def __init__(self, apikey):
        self.apikey = apikey

    # send request to api
    def request_api(self, opts):
        headers = {
            'Accept': "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
            'charset': "utf-8",
            'apikey': self.apikey,

        }

        url = 'https://api.ghasedak.me/v2/' + opts['path']

        data = opts['data']

        r = requests.post(url, data=data, headers=headers)

        return r

    def status(self, opts):
        data = {}
        data['path'] = "sms/status?agent=python"
        data['data'] = {
            'id': opts['id'],
            'type': opts['type']
        }
        
        r = self.request_api(data)

        
        jr = r.json()
        # print(jr["items"])
        
        if r.status_code == 200:
            return jr["items"]

        return []

    def send(self, opts):
        data = {}
        data['path'] = "sms/send/simple?agent=python"
        data['data'] = {
            'message': opts['message'],
            'receptor': opts['receptor'],
            'linenumber': opts['linenumber'] if 'linenumber' in opts.keys() else "",
            'senddate': opts['senddate'] if 'senddate' in opts.keys() else "",
            'checkid': opts['checkid'] if 'checkid' in opts.keys() else ""
        }

        r = self.request_api(data)

        # # Get status data right after sending
        # jdata = json.loads(r.text)
        # self.status({str(jdata['items'][0]), '1'})

        if r.status_code == 200:
            return True

        return False

    def bulk1(self, opts):
        data = {}
        data['path'] = "sms/send/bulk?agent=python"
        data['data'] = {
            'message': opts['message'],
            'receptor': opts['receptor'],
            'linenumber': opts['linenumber'] if 'linenumber' in opts.keys() else "",
            'senddate': opts['senddate'] if 'senddate' in opts.keys() else "",
            'checkid': opts['checkid'] if 'checkid' in opts.keys() else ""
        }

        r = self.request_api(data)
        if r.status_code == 200:
            return True

        return False

    def bulk2(self, opts):
        data = {}
        data['path'] = "sms/send/pair?agent=python"
        data['data'] = {
            'message': opts['message'],
            'receptor': opts['receptor'],
            'linenumber': opts['linenumber'] if 'linenumber' in opts.keys() else "",
            'senddate': opts['senddate'] if 'senddate' in opts.keys() else "",
            'checkid': opts['checkid'] if 'checkid' in opts.keys() else ""
        }

        r = self.request_api(data)
        if r.status_code == 200:
            return True

        return False

    def pair(self, opts):
        data = {}
        data['path'] = "sms/send/pair?agent=python"
        data['data'] = {
            'message': opts['message'],
            'receptor': opts['receptor'],
            'linenumber': opts['linenumber'] if 'linenumber' in opts.keys() else "",
            'senddate': opts['senddate'] if 'senddate' in opts.keys() else "",
            'checkid': opts['checkid'] if 'checkid' in opts.keys() else ""
        }

        r = self.request_api(data)
        if r.status_code == 200:
            return True

        return False

    def voicecall(self, opts):
        data = {}
        data['path'] = "voice/send?agent=python"
        data['data'] = {
            'message': opts['message'],
            'receptor': opts['receptor'],
            'senddate': opts['senddate'] if 'senddate' in opts.keys() else ""
        }

        r = self.request_api(data)
        if r.status_code == 200:
            return True

        return False

    def verification(self, opts):
        data = {}
        data['path'] = "verification/send/simple?agent=python"
        data['data'] = {
            'receptor': opts['receptor'],
            'type': opts['type'] if 'type' in opts.keys() else "",
            'template': opts['template'],
            'ip': opts['ip'] if 'ip' in opts.keys() else "",
            'param1': opts['param1'],
            'param2': opts['param2'] if 'param2' in opts.keys() else "",
            'param3': opts['param3'] if 'param3' in opts.keys() else ""
        }

        r = self.request_api(data)
        if r.status_code == 200:
            return True

        return False

    def check_verification(self, opts):
        data = {}
        data['path'] = "sms/check/verification?agent=python"
        data['data'] = {
            'receptor': opts['receptor'],
            'token': opts['token'],
            'ip': opts['ip'] if 'ip' in opts.keys() else ""
        }

        r = self.request_api(data)
        if r.status_code == 200:
            return True

        return False
