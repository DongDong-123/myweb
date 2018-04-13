from django.shortcuts import render
from django.http import HttpResponse
from . models import Goods
import os
from django.core.paginator import Paginator

def Goodslist(request):

	return render(request,'back/goods-list.html')

def Goodsadd(request):

	return render(request,'back/goodsadd.html')

def Goodsinsert(request):
	ob = Goods()
	ob.goods = request.POST.get('goodsname')
	ob.price = request.POST.get('price')
	ob.store = request.POST.get('store')
	ob.state = request.POST.get('state')
	ob.num = request.POST.get('num')

	return HttpResponse('goodsinsert')

def Goodsedit(request):

	return HttpResponse('goodsedit')

def Goodsdel(request):

	return HttpResponse('goodsdel')

def Goodsupdate(request):

	return HttpResponse('goodsupdate')








# def Goodlist(request):
# 	return render(request,'back/goods-list.html')

# def typeadd(request):
# 	ob = Types.objects.all()
# 	context = {'types':ob}
# 	return render(request, 'back/typeadd.html', context)

# def typeinsert(request):

# 	try:
# 		ob = Types()
# 		ob.name = request.POST.get('name')
# 		ob.pid = request.POST.get('pid')
# 		# print('ob.pid',ob.pid)
# 		if ob.pid == '0':
# 			ob.path = '0,'
# 		else:
# 			p = Types.objects.get(id=ob.pid)
# 			ob.path = p.path + ob.pid + ','
# 		ob.save()
# 		return HttpResponse('<script>alert("添加成功");location.href="/typelist"</script>')
# 	except:
# 		return HttpResponse('<script>alert("添加失败");location.href="/typelist"</script>')


# def typelist(request):
# 	ob = Types.objects.extra(select = {'paths':'concat(path, id)'}).order_by('paths')
# 	# print('ob',ob[0].name)
# 	for x in ob:
# 		n = len(x.path) - 2
# 		x.name = (n*'|--') + x.name

# 	context = {'typelist':ob}
# 	return render(request, 'back/typelist.html', context)

# def typeedit(request, tid):
# 	ob = Types.objects.get(id = tid)
# 	obs = Types.objects.all()
# 	context = {'tinfo':ob, 'types':obs}
# 	return render(request,'back/typeedit.html', context)

# def typedel(request, tid):
# 	try:
# 		ob = Types.objects.get(id = tid)
# 		ob.delete()
# 		return HttpResponse('<script>alert("删除成功");location.href="/typelist"</script>')
# 	except:
# 		return HttpResponse('<script>alert("删除失败");location.href="/typelist"</script>')

# def typeupdate(request):
# 	try:
# 		ob = Types.objects.get(id = request.POST['ttid'])
# 		print(ob.name)
# 		print(request.POST['name'])
# 		ob.name = request.POST['name']
# 		# ob.save()
# 		return HttpResponse('<script>alert("修改成功");location.href="/typelist"</script>')
# 	except:
# 		return HttpResponse('<script>alert("修改失败");location.href="/typelist"</script>')

# def goodsadd(request):
# 	return render(request, 'back/goodsadd.html')

# def orderlist(request):
# 	return render(request, 'back/orderlist.html')


# # def calendar(request):
# 	# return render(request,'back/404.html')
# 	return render(request,'back/calendar.html')

