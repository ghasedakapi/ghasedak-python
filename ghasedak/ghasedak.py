# -*- coding: utf-8 -*-
"""
	ghasedak.py
	~~~~~~~~~
	:copyright: (c) 2018 by Ghasedak ICT
	:license: BSD-3-Clause-Clear, see LICENSE for more details.
"""
import requests
import json

class Ghasedak:
    """docstring for Ghasedak."""
    def __init__(self, apikey):
        self.apikey = apikey

	# send request to api
	def request_api(opts):
		headers = {
			'Accept': "application/json",
			"Content-Type": "application/x-www-form-urlencoded",
			'charset': "utf-8",
			'apikey': self.apikey
		}

		url = 'https://api.ghasedak.io/v1/' + opts['path']

		data = opts['data']

		r = requests.post(url, data=data, headers=headers)

		return r

	def send(opts):
		data = {}
		data['path'] = "sms/send/simple"
		data['data'] = {
			'message': opts['message'],
			'receptor': opts['receptor'],
			'linenumber': opts['linenumber'],
			'senddate': opts['senddate'],
			'checkid': opts['checkid']
		}

		r = request_api(data)
		if r.status_code == 200 {
			return True
		}
		return False

	def bulk1(opts):
		data = {}
		data['path'] = "sms/send/bulk"
		data['data'] = {
			'message': opts['message'],
			'receptor': opts['receptor'],
			'linenumber': opts['linenumber'],
			'senddate': opts['senddate'],
			'checkid': opts['checkid']
		}

		r = request_api(data)
		if r.status_code == 200 {
			return True
		}
		return False

	def bulk2(opts):
		data = {}
		data['path'] = "sms/send/bulk2"
		data['data'] = {
			'message': opts['message'],
			'receptor': opts['receptor'],
			'linenumber': opts['linenumber'],
			'senddate': opts['senddate'],
			'checkid': opts['checkid']
		}

		r = request_api(data)
		if r.status_code == 200 {
			return True
		}
		return False

	def voicecall(opts):
		data = {}
		data['path'] = "voice/send"
		data['data'] = {
			'message': opts['message'],
			'receptor': opts['receptor'],
			'senddate': opts['senddate']
		}

		r = request_api(data)
		if r.status_code == 200 {
			return True
		}
		return False

	def template(opts):
		data = {}
		data['path'] = "sms/verify"
		data['data'] = {
			'receptor': opts['receptor'],
			'type': opts['type'],
			'template': opts['template'],
			'param1': opts['param1'],
			'param2': opts['param2'],
			'param3': opts['param3']
		}

		r = request_api(data)
		if r.status_code == 200 {
			return True
		}
		return False

	def verification(opts):
		data = {}
		data['path'] = "sms/send/verification"
		data['data'] = {
			'receptor': opts['receptor'],
			'type': opts['type'],
			'template': opts['template'],
			'ip': opts['ip'],
			'param1': opts['param1'],
			'param2': opts['param2'],
			'param3': opts['param3']
		}

		r = request_api(data)
		if r.status_code == 200 {
			return True
		}
		return False

	def check_verification(opts):
		data = {}
		data['path'] = "sms/check/verification"
		data['data'] = {
			'receptor': opts['receptor'],
			'token': opts['token'],
			'ip': opts['ip']
		}

		r = request_api(data)
		if r.status_code == 200 {
			return True
		}
		return False
