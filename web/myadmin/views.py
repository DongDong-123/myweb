from django.shortcuts import render
from django.http import HttpResponse
from . models import Users
import os
from django.conf import settings
# 分页
from django.core.paginator import Paginator
# 密码加密
from django.contrib.auth.hashers import make_password
# 验证密码
from django.contrib.auth.hashers import check_password


# Create your views here.
def myadmin(request):
	return render(request,'back/base.html')

def uadd(request):
	return render(request,'back/useradd.html')

def insert(request):
	ob = Users()
	# print('ob',ob)
	ob.username = request.POST.get('name')
	ob.password = make_password(request.POST.get('password'), None, 'pbkdf2_sha256')
	ob.email = request.POST.get('email')
	ob.state = request.POST.get('state')
	if not request.FILES.get('img'):
		ob.img =  settings.BASE_DIR+'static/public/img/9110.jpg'
	else:
		ob.img = request.FILES.get('img')


	ob.save()

	return HttpResponse("<script>alert('添加成功'),location.href='/myadmin/ulist'</script>")

def ulist(request):
	# 搜索
	
	v = request.GET.get('keywords','')
	arr = {
	1:['会员','会','员'],
	2:['禁用','禁','用'],
	3:['管理员','管理','管','理'],
	}
	state = 0
	for k,x in arr.items():
		if v in x:
			state = k

	from django.db.models import Q
	ob = Users.objects.filter(Q(id__contains=v)|Q(username__contains=v)|Q(email__contains=v)|Q(state__contains=state))
	
	# 分页
	paginator = Paginator(ob, 4)
	p = int(request.GET.get('p', 1))
	userlist = paginator.page(p)
	content = {'users':userlist, 'p':p}
	return render(request, 'back/userlist.html', content)

def udel(request,uid):
	ob = Users.objects.get(id=uid)
	del_img = ob.img
	ob.delete()
	path_img = "./"+ str(del_img)
	if str(del_img) !=  'static/public/img/9110.jpg':
		os.remove(settings.BASE_DIR+path_img)
	return HttpResponse("<script>alert('删除成功'),location.href='/myadmin/ulist'</script>")

def uedit(request, uid):
	ob = Users.objects.get(id=uid)
	content = {'oinfo':ob}
	# print(content)
	return render(request,'back/useredit.html',content)

def uupdate(request):
	ob = Users.objects.get(id=request.POST['id'])
	oc = Users()
	edit_img = ob.img
	ob.username = request.POST['name']
	ob.password = make_password(request.POST.get('password'), None, 'pbkdf2_sha256')
	ob.email = request.POST['email']
	ob.state = request.POST['state']
	print('dd',request.FILES.get('img'))
	if not request.FILES.get('img'):
		oc.img = str(edit_img)
	else:
		ob.img = request.FILES.get('img')
		path_img = "./" + str(edit_img)
		if str(edit_img) != 'static/public/img/9110.jpg':
			os.remove(settings.BASE_DIR+path_img)
	ob.save()
	return HttpResponse("<script>alert('修改成功'),location.href='/myadmin/ulist'</script>")

def login(request):
	return render(request,'back/login.html')

def dologin(request):
	if request.session['verifycode'] != request.POST.get('vcode'):
		return HttpResponse('<script>alert("验证码错误");location.href="/myadmin/login"</script>')
	try:
		ob = Users.objects.get(username = request.POST['username'])
		if ob.state == 0:
			if check_password(request.POST['password'],ob.password):
				request.session['AdminLoginS'] = {'uid':ob.id, 'username':ob.username,}
				return HttpResponse('<script>alert("登录成功");location.href="/myadmin/ulist"</script>')
			else:
				raise
		else:
			raise
	except:
		pass
	return HttpResponse("<script>alert('登录失败'),location.href='/myadmin/login'</script>")

def logout(request):
	request.session['AdminLoginS'] = {}
	return HttpResponse("<script>alert('已退出登录'),location.href='/myadmin/login'</script>")

def verifycode(request):
    from PIL import Image, ImageDraw, ImageFont
    import random
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 40
    im = Image.new('RGB', (width, height), bgcolor)
    draw = ImageDraw.Draw(im)
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # str1 = '你好啊我是管理员想登陆吗需要验证啊输入验证码吧哈'
    str1 = '123456789'
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    font = ImageFont.truetype('NotoSansCJK-Light.ttc', 23)
    # font = ImageFont.load_default().font
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    del draw
    request.session['verifycode'] = rand_str
    import io
    buf = io.BytesIO()
    im.save(buf, 'png')
    return HttpResponse(buf.getvalue(), 'image/png')
