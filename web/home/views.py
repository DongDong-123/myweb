from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import Goods,Types,Users,Orders,Detail
from myadmin.views import insert
from django.conf import settings
import time 

# 商城首页
# def index(request):
# 	return render(request, 'front/base.html')
# 用户注册
def regedit(request):
	ob = Users.objects.all()
	context = {'checkname':ob}
	return render(request, 'front/register.html',context)
# 注册验证
def checkregedit(request):
	inputname = request.GET.get('Nam')
	print('inputname',inputname)
	if Users.objects.filter(username=inputname):
		return HttpResponse('1')
	else:
		return HttpResponse('0')
# 插入注册信息
def insertregedit(request):
	try:
		ob = Users()
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
		return HttpResponse("<script>alert('注册成功');location.href='/user/index'</script>")
	except:
		return HttpResponse("<script>alert('注册失败');location.href='/user/index'</script>")
# 前台登录
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
					request.session['VipUser'] = {'uid':ob.id,'username':ob.username,'img':str(ob.img)}
					return HttpResponse('<script>alert("登录成功");location.href="/user/index"</script>')
				else:
					# 密码错误
					raise
		except:
			pass
	return HttpResponse('<script>alert("用户名或密码错误");location.href="login"</script>')
# 前台退出
def logout(request):
	request.session['VipUser'] = {}
	return HttpResponse("<script>alert('已退出登录'),location.href='/user/index'</script>")
# 商城首页
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
# 商品列表
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
	# ob = Types.objects.all()
	carts = request.session.get('cart',{})
	print('carts',carts)
	context = {'cart':carts}
	# context = {'cart':carts,'typelist':ob}
	return render(request,'front/cart.html',context)
# 购物车编辑
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
    # 选择购买的商品id
    ids = request.POST.get('idg','').split(',')
    print('ids2',ids)
    # # 购物车数据{6:{},5:{}}
    cart = request.session['cart']
    print('cart2',cart)

    # 组装已购买的商品数据
    order = []
    for x in ids:
        print('x2', x)
        order.append(cart[x])

    context = {'orders':order,'ids':ids}

    return render(request,'front/confimorder.html', context)
# 创建订单
def createorder(request):
    ids = request.POST.get('ids','').split(',')
    cart = request.session['cart']
    print('cartcreate',cart)
    totalprice = 0
    totalnum = 0
    for x in ids:
        print("cart[x]['price']",cart[x]['price'],type(cart[x]['price']))
        print("cart[x]['num']",cart[x]['num'],type(cart[x]['num']))
        totalprice += (cart[x]['price'] * cart[x]['num'])
        print('totalprice',totalprice)
        totalnum += cart[x]['num']
        print('totalnum',totalnum)

    od = Orders()
    # 收货信息 
    od.uid =  Users.objects.get(id=request.session['VipUser']['uid'])
    od.linkman = request.POST.get('linkman')
    od.address = request.POST.get('address')
    od.phone = request.POST.get('phone')
    od.code = request.POST.get('code')
    # 总价
    od.total = totalprice
    # 数量
    od.nums = totalnum
    # 状态
    od.status = 1
    # 打印测试
    # print('od.uid',od.uid,type(od.uid))
    # print('od.linkman',od.linkman,type(od.linkman))
    # print('od.address',od.address,type(od.address))
    # print('od.phone',od.phone,type(od.phone))
    # print('od.code',od.code,type(od.code))
    # print('od.totalprice',od.total,type(od.total))
    # print('od.nums',od.nums,type(od.nums))
    od.save()

    # 添加订单详情信息
    for x in ids:
        info = Detail()
        info.orderid = od
        info.goodsid = Goods.objects.get(id=x)
        info.num = cart[x]['num']
        info.name = cart[x]['goods']
        info.price = cart[x]['price']
        # 打印测试
        # print('info.orderid',info.orderid,type(info.orderid))
        # print('info.goodsid',info.goodsid,type(info.goodsid))
        # print('info.num',info.num,type(info.num))
        # print('info.price',info.price,type(info.price))
        info.save()
        # 删除购物车中对应的商品信息
        del cart[x]

    # 把购物车信息重新存入session中
    request.session['cart'] = cart
    # 跳转到付款页面
    return HttpResponse('<script>alert("下单成功");location.href="displayorder/'+str(od.id)+'"</script>')
# 订单确认
def displayorder(request,oid):
    # 添加订单详情信息
    ob = Orders.objects.get(id=oid)
    print(ob)
    context = {'odisplay':ob}
   
    return render(request,'front/displayorder.html',context)

# 提交订单
def payonline(request,oid):
    # 根据oid查询订单信息,展示付款页面
    ob = Orders.objects.get(id=oid)

    ob.status = 2
    
    return HttpResponse('<script>alert("付款成功");location.href="/cartindex"</script>')
# 用户中心
def personal(request):
	return render(request,'front/personal.html')
# 我的订单
def myorder(request):
	v = request.GET.get('keywords','')
	arr = {
	1:['已付款','已付'],
	2:['未付款','未','未付'],
	0:['已关闭','关闭','关','闭'],
	}
	state = 0
	for k,x in arr.items():
		if v in x:
			state = k

	from django.db.models import Q
	ob = Orders.objects.filter(Q(id__contains=v)|Q(linkman__contains=v)|Q(address__contains=v)|Q(phone__contains=v)|Q(code__contains=v)|Q(nums__contains=v)|Q(status__contains=state))

	buyer = request.session['VipUser']['username']
	# 测试数据
	# print('buyer',buyer)
	# ob = Orders.objects.all()
	# for i in ob:
	# 	print('ob',i,type(i))
	# 	# for v in i.uid:
	# 	print('v',i.uid.username,type(i.uid.username))
	# print(ob.uid)

	# # 分页
	from django.core.paginator import Paginator
	paginator = Paginator(ob, 10)
	p = int(request.GET.get('p', 1))
	orderlist = paginator.page(p)
	content = {'orderlist':orderlist, 'p':p,'buyer':buyer}

	return render(request,'front/myorder.html',content)





