from django.shortcuts import render
from django.http import HttpResponse
from . models import Types
import os
from django.core.paginator import Paginator

def Goodlist(request):
	return render(request,'back/goodslist.html')

def typeadd(request):
	ob = Types.objects.all()
	context = {'types':ob}
	return render(request, 'back/typeadd.html', context)

def typeinsert(request):
	try:
		ob = Types()
		ob.name = request.POST.get('name')
		ob.pid = request.POST.get('pid')
		# print('ob.pid',ob.pid)
		if ob.pid == '0':
			ob.path = '0,'
		else:
			p = Types.objects.get(id=ob.pid)
			ob.path = p.path + ob.pid + ','
		ob.save()
		return HttpResponse('<script>alert("添加成功");location.href="/myadmin/typelist"</script>')
	except:
		return HttpResponse('<script>alert("添加失败");location.href="/myadmin/typelist"</script>')

def typelist(request):
	context = {'typepage':Getpage(request)}
	return render(request, 'back/typelist.html', context)

def typedel(request, tid):
	try:
		ob = Types.objects.get(id = tid)
		ob.delete()
		return HttpResponse('<script>alert("删除成功");location.href="/myadmin/typelist"</script>')
	except:
		return HttpResponse('<script>alert("删除失败");location.href="/myadmin/typelist"</script>')

def typeedit(request, tid):
	ob = Types.objects.get(id = tid)
	obs = Types.objects.all()
	context = {'tinfo':ob, 'types':obs}
	return render(request,'back/typeedit.html', context)

def typeupdate(request):
	try:
		ob = Types.objects.get(id = request.POST['ttid'])
		# print(ob.name)
		# print(request.POST['name'])
		ob.name = request.POST['name']
		ob.save()
		return HttpResponse('<script>alert("修改成功");location.href="/myadmin/typelist"</script>')
	except:
		return HttpResponse('<script>alert("修改失败");location.href="/myadmin/typelist"</script>')

def goodsadd(request):
	return render(request, 'back/goodsadd.html')

def orderlist(request):
	return render(request, 'back/orderlist.html')


def Getpage(request):
	v = request.GET.get('keywords','')
	from django.db.models import Q
	ob = Types.objects.filter(Q(id__contains=v)|Q(name__contains=v))

	from django.core.paginator import Paginator
	for x in ob:
		n = len(x.path) - 2
		x.name = (n*'|--') + x.name
	paginator = Paginator(ob, 6)
	p = int(request.GET.get('p', 1))
	goodslist = paginator.page(p)
	return goodslist


