from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myadmin(request):
	# return HttpResponse('myadmin')
	return render(request,'back/login.html')