from django.shortcuts import render
from django.http import HttpResponse
from . models import Users ,Turnimg
import os
from django.conf import settings
# 分页
from django.core.paginator import Paginator
# 密码加密
from django.contrib.auth.hashers import make_password
# 验证密码
from django.contrib.auth.hashers import check_password


# 首页
def myadmin(request):
	return render(request,'back/base.html')

# 用户添加
def uadd(request):
	return render(request,'back/useradd.html')

# 用户插入
def insert(request):
	ob = Users()
	# print('ob',ob)
	ob.username = request.POST.get('name')
	ob.password = make_password(request.POST.get('password'), None, 'pbkdf2_sha256')
	ob.email = request.POST.get('email')
	ob.state = request.POST.get('state')
	if not request.FILES.get('img'):
		ob.img = 'static/public/img/9110.jpg'
	else:
		ob.img = request.FILES.get('img')
	ob.save()

	return HttpResponse("<script>alert('添加成功'),location.href='/myadmin/ulist'</script>")

# 用户列表
def ulist(request):
	# 搜索
	v = request.GET.get('keywords','')
	arr = {
	1:['会员','会','员'],
	2:['禁用','禁','用'],
	0:['管理员','管理','管','理'],
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

# 用户删除
def udel(request,uid):
	ob = Users.objects.get(id=uid)
	del_img = ob.img
	ob.delete()
	path_img = "./"+ str(del_img)
	if str(del_img) !=  'static/public/img/9110.jpg':
		os.remove(path_img)
	return HttpResponse("<script>alert('删除成功'),location.href='/myadmin/ulist'</script>")

# 用户编辑
def uedit(request, uid):
	ob = Users.objects.get(id=uid)
	content = {'oinfo':ob}
	return render(request,'back/useredit.html',content)
	
# 用户更新
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
			os.remove(path_img)
	ob.save()
	return HttpResponse("<script>alert('修改成功'),location.href='/myadmin/ulist'</script>")

# 后台登录
def login(request):
	return render(request,'back/login.html')

# 执行登录
def dologin(request):
	if request.session['verifycode'] != request.POST.get('vcode'):
		return HttpResponse('<script>alert("验证码错误");location.href="/myadmin/login"</script>')
	try:
		ob = Users.objects.get(username = request.POST['username'])
		if ob.state == 0:
			if check_password(request.POST['password'],ob.password):
				request.session['AdminLoginS'] = {'uid':ob.id, 'username':ob.username,'img':str(ob.img)}
				return HttpResponse('<script>alert("登录成功");location.href="/myadmin/ulist"</script>')
			else:
				raise
		else:
			raise
	except:
		pass
	return HttpResponse("<script>alert('登录失败'),location.href='/myadmin/login'</script>")

# 后台退出
def logout(request):
	request.session['AdminLoginS'] = {}
	return HttpResponse("<script>alert('已退出登录'),location.href='/myadmin/login'</script>")

# 验证码
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

# 轮播图列表
def turnindex(request):
	ob = Turnimg.objects.all()
	context = {'allimg':ob }
	return render(request,'back/turnindex.html',context)

# 轮播图控制
def turnimg(request):
	ob = Turnimg.objects.all()
	context = {'allimg':ob }
	return render(request,'back/turnimgedit.html',context)

# 轮播图插入
def insertturnimg(request):
	print('aa')
	try:
		ob = Turnimg()
		ob.img = request.FILES.get('img')
		print('img',ob.img)
		ob.save()
		return HttpResponse("<script>alert('上传成功'),location.href='/myadmin/'</script>")
	except:
		return HttpResponse("<script>alert('上传失败'),location.href='/myadmin/'</script>")

# 轮播图替换
def changeimg(request):
	ob = Turnimg.objects.all()
	context = {'allimg':ob }
	return render(request,'back/changeimg.html',context)

# 轮播图更新
def imgupdate(request):
	ob = Turnimg.objects.get(id=request.POST.get('turnimg'))
	# print(ob)
	ob.img = request.FILES.get('img')
	ob.save()
	return HttpResponse("<script>alert('上传成功'),location.href='/myadmin/changeimg'</script>")

# 轮播图删除
def delimg(request):
	ob = Turnimg.objects.all()
	context = {'allimg':ob }
	return render(request,'back/delimg.html',context)

# 执行删除
def imgsdel(request):
	ob = Turnimg.objects.get(id=request.POST.get('turnimg'))
	ob.delete()
	return HttpResponse("<script>alert('删除成功'),location.href='/myadmin/delimg'</script>")









