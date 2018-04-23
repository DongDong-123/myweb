from django.shortcuts import render
from django.http import HttpResponse
import re

class AdminLoginMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		urllist = ['/myadmin/login','/myadmin/dologin','/myadmin/logout', '/myadmin/verifycode']
		print('我是后台中间件')
		if re.match('/myadmin/',request.path) and request.path not in urllist:
			if not request.session.get('AdminLoginS', ''):
				return HttpResponse('<script>alert("请登录");location.href="/myadmin/login";</script>')


		userurls = ['/user/createorder/','/user/confimorder/','/user/displayorder/','/user/payonline','/user/personal']
		print('我是前台中间件')

		# if re.match('/user/personal',request.path):
		if request.path in userurls:
		# 检测是否登录
			if not request.session.get('VipUser',''):
				# 如果在session没有记录,则证明没有登录,跳转到登录页面
				return HttpResponse('<script>alert("请先登录");location.href="/user/login/";</script>')

		response = self.get_response(request)
		return response
