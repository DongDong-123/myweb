from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import Goods,Types,Users,Orders,Detail
from myadmin.views import insert
from django.conf import settings
import time 


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
		ob.img = request.FILES.get('img')

	ob.save()
	return HttpResponse("<script>alert('注册成功');location.href=‘/user/index'</script>")

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

def index(request):
	t = Types.objects.filter(pid=0)
	arr = []
	for v in t:
		v.sub = Types.objects.filter(pid = v.id)
		for x in v.sub:
			x.sub = Goods.objects.filter(typeid_id = x.id)
		arr.append(v)

	data = Types.objects.all()
	glist_ob = Goods.objects.all()
	context = {'typelist':data,'typegood':arr,'glist':glist_ob}

	return render(request,'front/index.html',context)

def goodslist(request,tid, tpid):
	t = Types.objects.filter(pid=0)
	if tpid == '0':
		attr = []
		top = Types.objects.filter(pid=tid)
		data = Goods.objects.filter(typeid_id=top[0].id)
	else:
		data = Goods.objects.filter(typeid_id=tid)

	context = {'typelist':t,'goodslist':data}
	return render(request,'front/goodslist.html',context)

# 商品详情
def goods(request,tid):
	ob = Goods.objects.get(id=tid)
	context = {"goodsinfo":ob}

	return render(request,'front/goods.html',context)

# 添加购物车
def cartadd(request):
	gid = request.POST.get('pid')
	num = int(request.POST['numbs'])
	ob = Goods.objects.get(id=gid)
	data = request.session.get('cart',{})
	if gid in data.keys():
		data[gid]['num']+=num
	else:
		arr = {'goods':ob.goods,'price':float(ob.price),'id':ob.id,'picname':ob.picname,'num':num}
		data[gid]=arr

	request.session['cart'] = data
	return HttpResponse('<script>location.href="cartindex"</script>')

# 购物车列表
def cartindex(request):
	ob = Types.objects.all()
	carts = request.session.get('cart',{})
	print('carts',carts)
	context = {'cart':carts,'typelist':ob}
	return render(request,'front/cart.html',context)

def cartedit(request):
	gid = request.GET.get('gid',None)
	num = request.GET.get('num',None)
	print('num',num,type(num))
	print('gid',gid,type(gid))

	cart = request.session.get('cart',{})
	cart[gid]['num'] = int(num)
	request.session['cart'] = cart
	return HttpResponse('0')

# 删除购物车商品
def cartdel(request):
	pid = request.GET.get('Pid')
	delcart = request.session.get('cart',{})
	del delcart[pid]
	request.session['cart'] = delcart
	return HttpResponse('<script>location.href="/"</script>')
# 确认订单
def confimorder(request):
	ob = Types.objects.all()
	carts = request.session.get('cart',{})
	print('carts',carts)
	context = {'cart':carts,'typelist':ob}

	return render(request,'front/confimorder.html', context)

def createorder(request):
	
    od = Orders()
    # 收货信息 
    od.uid =  request.POST.get('pid')
    print('od.uid',od.uid,type(od.uid))
    od.linkman = request.POST.get('linkman')
    print('od.linkman',od.linkman)
    od.address = request.POST.get('address')
    od.phone = request.POST.get('phone')
    od.code = request.POST.get('code')
    # 总价
    od.total = request.POST.get('total')
    print('od.totalprice',od.total)
    od.nums = request.POST.get('totalCount')
    
    # 状态
    od.status = 1

    od.save()

    # 再去添加订单详情信息
    ob = Orders.objects.all()
    print(ob)
    # for x in ids:
    #     info = OrderInfo()
    #     info.orderid = od
    #     info.gid = Goods.objects.get(id=x)
    #     info.num = cart[x]['num']
    #     info.price = cart[x]['price']
    #     info.save()
    #     # 购物车中对应的商品信息
    #     del cart[x]

    # 把购物车信息重新存入session中
    # request.session['cart'] = cart


    # 跳转到付款页面
    return HttpResponse('<script>alert("下单成功");location.href="displayorder"</script>')

def displayorder(request):
    # 再去添加订单详情信息
    ob = Orders.objects.all()
    print(ob)
    data = request.session.get('cart', {})
    for v in data.values():
        print(v.price)
    for i in ob:
        print(i)
        info = Detail()
        info.orderid = i.id
        info.goodsid = i.uid
        info.price = request.session.get(id=)
        info.num = i.nums
    # for x in ids:
    #     info = OrderInfo()
    #     info.orderid = od
    #     info.gid = Goods.objects.get(id=x)
    #     info.num = cart[x]['num']
    #     info.price = cart[x]['price']
    #     info.save()
    #     # 购物车中对应的商品信息
    #     del cart[x]

    # 把购物车信息重新存入session中
    # request.session['cart'] = cart

    return HttpResponse('pay')
# 提交订单
def payonline(request):
	# oinfo = Orders.objects.get(id)
	oinfo.uid = Users.objects.get(id=request.session['VipUser']['uid'])
	oinfo.linkman = request.POST.get('linkman')
	oinfo.phone = request.POST.get('phone')
	oinfo.address = request.POST.get('address')
	oinfo.code = request.POST.get('code')
	# oinfo.total = 
	# oinfo.save()

	ob = Types.objects.all()
	carts = request.session.get('cart',{})
	context = {'cart':carts,'typelist':ob}

	return render(request, 'front/payonline.html', context)

