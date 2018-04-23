from django.shortcuts import render
from django.http import HttpResponse
from . models import Orders
import os
from django.core.paginator import Paginator


# 订单列表
def Orderlist(request):
	# 搜索
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
	# 分页
	paginator = Paginator(ob, 6)
	p = int(request.GET.get('p', 1))
	orderlist = paginator.page(p)
	content = {'orderlist':orderlist, 'p':p}
	return render(request, 'back/orderlist.html',content)
# 订单编辑
def Orderedit(request, tid):
	ob = Orders.objects.get(id = tid)
	# obs = Orders.objects.all()
	context = {'tinfo':ob}
	return render(request,'back/orderedit.html', context)
# 订单更新
def Orderupdate(request):
	try:
		ob = Orders.objects.get(id = request.POST.get('id'))
		print(ob.status)
		print(request.POST['id'])
		ob.status = request.POST['state']
		ob.save()
		return HttpResponse('<script>alert("修改成功");location.href="/myadmin/orderlist"</script>')
	except:
		return HttpResponse('<script>alert("修改失败");location.href="/myadmin/orderlist"</script>')

