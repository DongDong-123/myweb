from django.shortcuts import render
from django.http import HttpResponse
from . models import Goods,Types
import os, time


# 商品列表
def Goodslist(request):
	# 搜索
	v = request.GET.get('keywords','')
	arr = {
	1:['新品','新','品'],
	2:['在售','在','售'],
	0:['已下架','已','下','架'],
	}
	state = 0
	for k,x in arr.items():
		if v in x:
			state = k

	from django.db.models import Q
	ob = Goods.objects.filter(Q(id__contains=v)|Q(goods__contains=v)|Q(typeid__name__contains=v)|Q(price__contains=v)|Q(state__contains=state))
	# 分页
	from django.core.paginator import Paginator
	paginator = Paginator(ob, 6)
	p = int(request.GET.get('p', 1))
	goodslist = paginator.page(p)


	context = {'goods':goodslist, 'p':p}

	return render(request,'back/goodslist.html',context)
# 商品添加
def Goodsadd(request):
	obs = Types.objects.all()
	context = {'types':obs}
	return render(request,'back/goodsadd.html', context)

# 商品插入
def Goodsinsert(request):
	try:
		ob = Goods()
		ob.typeid = Types.objects.get(id = request.POST['pid'])
		print('ob.typeid',ob.typeid,type(ob.typeid))
		ob.goods = request.POST.get('goodsname')
		ob.price = request.POST.get('price')
		ob.store = request.POST.get('store')
		ob.state = request.POST.get('state')
		ob.descr = request.POST.get('content')
		ob.picname = upload(request)
		ob.save()

		return HttpResponse('<script>alert("添加成功"); location.href="/myadmin/goodslist"</script>')
	except Exception as e:
		print(Exception,e)
		return HttpResponse('<script>alert("添加失败"); location.href="/myadmin/goodslist"</script>')

# 商品删除
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
	
# 商品编辑
def Goodsedit(request, gid):
	obs = Types.objects.all()
	ob = Goods.objects.get(id=gid)
	oc = str(ob.typeid_id)
	print('oc',oc)
	context = {'editinfo':ob, 'types':obs}
	print("ob",ob.typeid_id)
	return render(request,'back/goodsedit.html', context)

# 商品更新
def Goodsupdate(request):
	try:
		ob = Goods.objects.get(id=request.POST.get('id'))
		pic = ob.picname
		ob.typeid = Types.objects.get(id = request.POST['pid'])
		ob.goods = request.POST.get('goodsname')
		ob.price = request.POST.get('price')
		ob.store = request.POST.get('store')
		ob.state = request.POST.get('state')
		ob.descr = request.POST.get('content')
		ob.picname = upload(request)
		oldpic = "."+str(pic)
		if oldpic:
			os.remove(oldpic)
		ob.save()

		return HttpResponse('<script>alert("修改成功"); location.href="/myadmin/goodslist"</script>')
	except Exception as e:
		print(Exception,e)
		return HttpResponse('<script>alert("修改失败"); location.href="/myadmin/goodslist"</script>')

# 上传图片函数
def upload(request):
	myfile = request.FILES.get("img", None)
	filename = str(time.time())+"."+myfile.name.split(".").pop()
	up = open("./static/public/img/"+filename,"wb+")
	for chunk in myfile.chunks():
		up.write(chunk)
	up.close()
	return "/static/public/img/"+filename

