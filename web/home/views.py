from django.shortcuts import render
from django.http import HttpResponse
from . models import Users
# Create your views here.
def index(request):
	return render(request, 'front/index.html')

def regedit(request):
	ob = Users.objects.all()
	context = {'checkname':ob}
	return render(request, 'front/regedit.html',context)

def checkregedit(request):
	# ob = Users()

	return HttpResponse('注册验证')

def login(request):
	return render(request, 'front/login.html')

# def checkname(request):
