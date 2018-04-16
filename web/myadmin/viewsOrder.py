from django.shortcuts import render
from django.http import HttpResponse
from . models import Orders
import os
from django.core.paginator import Paginator



def Orderlist(request):
	
	return render(request, 'back/orderlist.html')

def Orderadd(request):
	
	return render(request, 'back/Orderadd.html', context)

def Orderinsert(request):

	try:
		ob = Orders()
		ob.name = request.POST.get('name')
		ob.pid = request.POST.get('pid')
		# print('ob.pid',ob.pid)
		if ob.pid == '0':
			ob.path = '0,'
		else:
			p = Orders.objects.get(id=ob.pid)
			ob.path = p.path + ob.pid + ','
		ob.save()
		return HttpResponse('<script>alert("添加成功");location.href="/Orderlist"</script>')
	except:
		return HttpResponse('<script>alert("添加失败");location.href="/Orderlist"</script>')

def Orderedit(request, tid):
	ob = Orders.objects.get(id = tid)
	obs = Orders.objects.all()
	context = {'tinfo':ob, 'Orders':obs}
	return render(request,'back/Orderedit.html', context)

def Orderdel(request, tid):
	try:
		ob = Orders.objects.get(id = tid)
		ob.delete()
		return HttpResponse('<script>alert("删除成功");location.href="/Orderlist"</script>')
	except:
		return HttpResponse('<script>alert("删除失败");location.href="/Orderlist"</script>')

def Orderupdate(request):
	try:
		ob = Orders.objects.get(id = request.POST['ttid'])
		print(ob.name)
		print(request.POST['name'])
		ob.name = request.POST['name']
		# ob.save()
		return HttpResponse('<script>alert("修改成功");location.href="/Orderlist"</script>')
	except:
		return HttpResponse('<script>alert("修改失败");location.href="/Orderlist"</script>')

def goodsadd(request):
	return render(request, 'back/goodsadd.html')

