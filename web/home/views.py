from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import Goods,Types,Users
# Create your views here.
def index(request):
	return render(request, 'front/base.html')

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

def index(request):
	t = Types.objects.filter(pid=0)
	arr = []
	for v in t:
		v.sub = Types.objects.filter(pid = v.id)
		for x in v.sub:
			x.sub = Goods.objects.filter(typeid_id = x.id)
		arr.append(v)

	# print(arr)
	data = Types.objects.exclude(pid=0)
	# print(data)

	for i in arr:
		print('arr',i,type(i))
		print('arr',i.name,type(i.name))
		for ii in i.sub:
			print('ii',ii)

	glist_ob = Goods.objects.all()
	print(glist_ob)
	context = {'typelist':data,'typegood':arr,'glist':glist_ob}


	return render(request,'front/index.html',context)

def goodslist(request):
	# t = Types.objects.filter(pid=0)
	# arr = []
	# for v in t:
	# 	v.sub = Types.objects.filter(pid = v.id)
	# 	for x in v.sub:
	# 		x.sub = Goods.objects.filter(typeid_id = x.id)
	# 	arr.append(v)

	data = Types.objects.exclude(pid=0)

	context = {'typelist':data}


	return render(request,'front/goodslist.html',context)

def goods(request):

	
	return render(request,'front/goods.html')
