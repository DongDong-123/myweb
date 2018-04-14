from django.shortcuts import render
from django.http import HttpResponse
from . models import Goods,Types
import os, time
from django.core.paginator import Paginator

def Goodslist(request):
	ob = Goods.objects.all()
	paginator = Paginator(ob, 3)
	p = int(request.GET.get('p', 1))
	goodslist = paginator.page(p)
	context = {'goods':goodslist, 'p':p}

	return render(request,'back/goodslist.html',context)
	
def Goodsadd(request):
	obs = Types.objects.all()
	context = {'types':obs}

	return render(request,'back/goodsadd.html', context)

def Goodsinsert(request):
	try:
		ob = Goods()
		ob.typeid = Types.objects.get(id = request.POST['pid'])
		ob.goods = request.POST.get('goodsname')
		ob.price = request.POST.get('price')
		ob.store = request.POST.get('store')
		ob.state = request.POST.get('state')
		ob.picname = upload(request)
		ob.save()

		return HttpResponse('<script>alert("添加成功"); location.href="/myadmin/goodslist"</script>')
	except Exception as e:
		print(Exception,e)
		return HttpResponse('<script>alert("添加失败"); location.href="/myadmin/goodslist"</script>')

def Goodsedit(request, gid):
	obs = Types.objects.all()
	ob = Goods.objects.get(id=gid)
	oc = str(ob.typeid)
	print('oc',oc)
	context = {'editinfo':ob, 'types':obs}
	# print("obs",obs.pid)
	print("ob",ob.typeid)

	return render(request,'back/goodsedit.html', context)

def Goodsdel(request, gid):
	try:
		ob = Goods.objects.get(id = gid)
		picpath = "." + str(ob.picname)
		if picpath:
			os.remove(picpath)
		ob.delete()
		return HttpResponse('<script>alert("删除成功"); location.href="/myadmin/goodslist"</script>')
	except Exception as e:
		print(Exception,e)
		return HttpResponse('<script>alert("删除失败"); location.href="/myadmin/goodslist"</script>')

	return HttpResponse('goodsdel')

def Goodsupdate(request):
	try:
		ob = Goods.objects.get(id=request.POST.get('id'))
		pic = ob.picname
		ob.typeid = Types.objects.get(id = request.POST['pid'])
		ob.goods = request.POST.get('goodsname')
		ob.price = request.POST.get('price')
		ob.store = request.POST.get('store')
		ob.state = request.POST.get('state')
		ob.picname = upload(request)
		oldpic = "."+str(pic)
		if oldpic:
			os.remove(oldpic)
		ob.save()

		return HttpResponse('<script>alert("修改成功"); location.href="/myadmin/goodslist"</script>')
	except Exception as e:
		print(Exception,e)
		return HttpResponse('<script>alert("修改失败"); location.href="/myadmin/goodslist"</script>')

def upload(request):
	myfile = request.FILES.get("img", None)
	filename = str(time.time())+"."+myfile.name.split(".").pop()
	up = open("./static/public/img/"+filename,"wb+")
	for chunk in myfile.chunks():
		up.write(chunk)
	up.close()
	
	return "/static/public/img/"+filename

