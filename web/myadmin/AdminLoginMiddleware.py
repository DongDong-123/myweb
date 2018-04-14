from django.shortcuts import render
from django.http import HttpResponse
import re

class AdminLoginMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		urllist = ['/myadmin/login','/myadmin/dologin','/myadmin/logout', '/myadmin/verifycode']
		if re.match('/myadmin/',request.path) and request.path not in urllist:
			if not request.session.get('AdminLoginS', ''):
				return HttpResponse('<script>alert("请登录");location.href="/myadmin/login";</script>')


		response = self.get_response(request)
		return response
