from django.shortcuts import render
from django.http import HttpResponse
from . models import Users
import os
from django.core.paginator import Paginator

def Goodlist(request):
	return render(request,'back/goods-list.html')

def typeadd(request):
	return render(request, 'back/typeadd.html')

def typeinsert(request):




	return HttpResponse('typeinsert')

def typelist(request):
	return render(request, 'back/typelist.html')

def goodsadd(request):
	return render(request, 'back/goodsadd.html')

def orderlist(request):
	return render(request, 'back/orderlist.html')


# def calendar(request):
	# return render(request,'back/404.html')
	return render(request,'back/calendar.html')

# def chart(request):

# 	return render(request,'back/chart.html')

# def form(request):

# 	return render(request,'back/form.html')

# def login(request):

# 	return render(request,'back/login.html')

# def sign_up(request):

# 	return render(request,'back/sign-up.html')

# def table_list_img(request):

# 	return render(request,'back/table-list-img.html')

# def table_list(request):

# 	return render(request,'back/table-list.html')

# def tables(request):

# 	return render(request,'back/tables.html')
