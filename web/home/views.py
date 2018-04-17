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
	if Users.objects.filter(username=data):

		return HttpResponse('注册失败')
	else:


		return HttpResponse('注册验证')

def login(request):
	return render(request, 'front/regedit.html')

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
	data = Types.objects.all()
	# for v in data:
	# 	print('v',v)
	# 	print('v.pid',v.pid)
	# print(data)

	# for i in arr:
	# 	print('arr',i,type(i))
	# 	print('arr.name',i.name,type(i.name))
	# 	print('arr.id',i.id,type(i.id))
	# 	for ii in i.sub:
	# 		print('ii',ii)
	# 		print('ii.id',ii.id)

	glist_ob = Goods.objects.all()
	# print(glist_ob)
	context = {'typelist':data,'typegood':arr,'glist':glist_ob}


	return render(request,'front/index.html',context)

def goodslist(request,tid, tpid):
	t = Types.objects.filter(pid=0)
	# arr = []
	# for v in t:
	# 	v.sub = Types.objects.filter(pid = v.id)
	# 	for x in v.sub:
	# 		x.sub = Goods.objects.filter(typeid_id = x.id)
	# 	arr.append(v)

	# data = Goods.objects.filter(state=2)
	if tpid == '0':
		attr = []
		top = Types.objects.filter(pid=tid)
		# top = Types.objects.exclude(pid=0)
		# print('top0',top)
		# print('top0',top[0].pid,type(top[0]))
		for i in top:
		# 	print(i.pid,i.id)
		# 	return i.id
			attr.append(i.id)
		print('attr',attr)
		# print('i.id',i.id)
		data = Goods.objects.filter(typeid_id=top[0].id)
		# data = Goods.objects.all()
		print('data1',data)
		for i in data:
			print('state1',i.state)
			print('goods1',i.goods)
	else:
		data = Goods.objects.filter(typeid_id=tid)
		print('data2',data)
		for i in data:
			print('state2',i.state)
			print('goods2',i.goods)

	context = {'typelist':t,'goodslist':data}


	return render(request,'front/goodslist.html',context)

def goods(request,tid):
	ob = Goods.objects.get(id=tid)
	print("ob",ob,type(ob))
	print(ob.id,ob.goods)

	context = {"goodsinfo":ob} 
	
	return render(request,'front/goods.html',context)


def cartindex(request,tid):
	# ob = Goods.objects.get(id=tid)
	# print(ob)
	# context = {'cartinfo':ob}
	ob = Types.objects.all()
	cart = request.session.get('cart')
	context = {'cart':cart,'typelist':ob}
	return render(request,'front/cart.html',context)


def cartadd(request):
	goodsnum = request.POST['numbs']
	gid = int(request.POST.get('pid'))
	print('goodsnum',goodsnum)
	print('gid',gid,type(gid))
	ob = Goods.objects.get(id=gid)
	print(ob)
	print(ob.goods,ob.price,type(ob.goods))
	request.session['cartnumbe']=goodsnum
	request.session['cartname']=ob.goods
	request.session['cartprice']=ob.price



	return HttpResponse('<script>alert("添加成功")</script>')
