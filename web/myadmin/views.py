from django.shortcuts import render
from django.http import HttpResponse
from . models import Users
import os
from django.core.paginator import Paginator

# Create your views here.
def myadmin(request):
	# return HttpResponse('myadmin')
	return render(request,'back/index.html')

def uadd(request):
	return render(request,'back/add.html')

def insert(request):
	ob = Users()
	print('ob',ob)
	ob.username = request.POST.get('name')
	ob.password = request.POST.get('password')
	ob.email = request.POST.get('email')
	ob.state = request.POST.get('state')
	if request.FILES.get('img') is False:
		ob.img =  'static/public/img/9110.jpg'
	else:
		ob.img =  request.FILES.get('img')

	ob.save()
	# return HttpResponse('insert')
	return HttpResponse("<script>alert('添加成功'),location.href='/ulist'</script>")

def ulist(request):
	# 获取数据
	ob = Users.objects.all()
	# 实例化分页类
	paginator = Paginator(ob, 2)
	# 获取当前页码
	p = int(request.GET.get('p', 1))
	# 获取分页数据对象
	userlist = paginator.page(p)
	# 分配数据
	# content = {'users':ob}
	content = {'users':userlist, 'p':p}
	return render(request, 'back/user_list.html', content)

def udel(request,uid):
	ob = Users.objects.get(id=uid)
	del_img = ob.img
	ob.delete()
	path_img = "./"+ str(del_img)
	if str(del_img) !=  'static/public/img/9110.jpg':
		os.remove(path_img)
	return HttpResponse("<script>alert('删除成功'),location.href='/ulist'</script>")

def uedit(request, uid):
	ob = Users.objects.get(id=uid)
	content = {'oinfo':ob}
	# print(content)
	return render(request,'back/edit.html',content)


def uupdate(request):
	ob = Users.objects.get(id=request.POST['id'])
	oc = Users()
	edit_img = ob.img
	ob.username = request.POST['name']
	ob.password = request.POST['password']
	ob.email = request.POST['email']
	ob.state = request.POST['state']
	print('dd',request.FILES.get('img'))
	if request.FILES.get('img') is None:
		oc.img = str(edit_img)
	else:
		ob.img = request.FILES.get('img')
		path_img = "./" + str(edit_img)
		if str(edit_img) != 'static/public/img/9110.jpg':
			os.remove(path_img)
	ob.save()
	return HttpResponse("<script>alert('修改成功'),location.href='/ulist'</script>")





	

def calendar(request):
	# return render(request,'back/404.html')
	return render(request,'back/calendar.html')

def chart(request):

	return render(request,'back/chart.html')

def form(request):

	return render(request,'back/form.html')

def login(request):

	return render(request,'back/login.html')

def sign_up(request):

	return render(request,'back/sign-up.html')

def table_list_img(request):

	return render(request,'back/table-list-img.html')

def table_list(request):

	return render(request,'back/table-list.html')

def tables(request):

	return render(request,'back/tables.html')
