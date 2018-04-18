from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import Goods,Types,Users
from myadmin.views import insert
# Create your views here.
def index(request):
	return render(request, 'front/base.html')

def regedit(request):
	ob = Users.objects.all()
	context = {'checkname':ob}
	return render(request, 'front/register.html',context)

def checkregedit(request):
	inputname = request.GET.get('Nam')
	print('inputname',inputname)
	if Users.objects.filter(username=inputname):
		return HttpResponse('1')
	else:
		return HttpResponse('0')

def insertregedit(request):
	# insert()
	ob = Users()
	print('ob',ob)
	ob.username = request.POST.get('name')
	from django.contrib.auth.hashers import make_password
	ob.password = make_password(request.POST.get('password'), None, 'pbkdf2_sha256')
	aa = request.POST.get('password2')
	ob.email = request.POST.get('email')
	ob.state = request.POST.get('state')
	if not request.FILES.get('img'):
		ob.img =  'static/public/img/9110.jpg'
	else:
		ob.img =  request.FILES.get('img')
	ob.save()
	print("11222")
	return HttpResponse("<script>alert('注册成功');location.href=‘/user/index'</script>")
	# return HttpResponse('1122')

def login(request):
	if request.method == 'GET':
		return render(request,'front/login.html')
	else:
		try:
		# 接收用户名和密码,检测是否正确
			ob = Users.objects.get(username=request.POST['username'])
			# print('user',request.POST['username'])
	
			if ob.state != 2:
				# 检测密码是否正确
				from django.contrib.auth.hashers import check_password
				# 验证密码
				res = check_password(request.POST['password'],ob.password)
				# print(res)
				# print('password1',request.POST['password'])
				# print('password2',ob.password)
				# print('username',ob.username)
				# print('id',ob.id)
	
			# 判断密码是否正确
				if res:
				# 登录成功,用户信息.,记录到session,跳转地址
					print('res')
					request.session['VipUser'] = {'uid':ob.id,'username':ob.username}
					return HttpResponse('<script>alert("登录成功");location.href="/user/index"</script>')
				else:
					# 密码错误
					raise

		except:
			pass
	return HttpResponse('<script>alert("用户名或密码错误");location.href="login"</script>')
	


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


def cartindex(request):
	
	ob = Types.objects.all()
	carts = request.session.get('cart',{})
	# print('cart',carts,type(carts))
	
	context = {'cart':carts,'typelist':ob}

	return render(request,'front/cart.html',context)


def cartadd(request):
	gid = request.POST.get('pid')
	num = int(request.POST['numbs'])
	print('goodsnum',num)
	print('gid',gid,type(gid))
	ob = Goods.objects.get(id=gid)
	print('ob',ob)
	print(ob.goods,ob.price,type(ob.goods))
	
	data = request.session.get('cart',{})
	if gid in data.keys():
		data[gid]['num']+=num
	else:
		arr = {'goods':ob.goods,'price':float(ob.price),'id':ob.id,'picname':ob.picname,'num':num}
		data[gid]=arr

	request.session['cart'] = data
	print('data',data)
	# data {
	# '16': {'id': 16, 'num': '1', 'price': 2222.0, 'goods': '魅蓝 D4', 'picname': '/static/public/img/1523885717.8602414.jpg'},
	# '6': {'id': 6, 'num': '1', 'price': 4299.0, 'goods': '魅蓝 Note5', 'picname': '/static/public/img/1523885109.1853251.jpg'},
	# '14': {'id': 14, 'num': '344', 'price': 3222.0, 'goods': '魅蓝 X3', 'picname': '/static/public/img/1523885622.854606.jpg'},
	# '19': {'id': 19, 'num': '1', 'price': 3355.0, 'goods': '魅蓝 A5', 'picname': '/static/public/img/1523885892.480298.jpg'},
	# '17': {'id': 17, 'num': '11', 'price': 3333.0, 'goods': '魅蓝 A9', 'picname': '/static/public/img/1523885792.198914.jpg'}
	# }

	return HttpResponse('<script>location.href="cartindex"</script>')

def cartdel(request,tid):
	delcart = request.session.get('cart',{})
	del cart[tid]
	request.session['cart'] = delcart

