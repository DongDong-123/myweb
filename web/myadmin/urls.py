"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views, viewsGoods

urlpatterns = [
    url(r'^myadmin/', views.myadmin, name='myadmin'),
    # url(r'^calendar/', views.calendar, name='calendar'),
    # url(r'^chart/', views.chart, name='chart'),
    # url(r'^form/', views.form, name='form'),
    # url(r'^login/', views.login, name='login'),
    # url(r'^sign_up/', views.sign_up,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   name='sign_up'),
    url(r'^table_list_img/', views.table_list_img, name='table_list_img'),
    url(r'^table_list/', views.table_list, name='table_list'),
    # url(r'^tables/', views.tables, name='tables'),
    url(r'^uadd/', views.uadd, name='uadd'),
    url(r'^insert/', views.insert, name='insert'),
    url(r'^ulist/', views.ulist, name='ulist'),
    url(r'^udel/(?P<uid>[0-9]+)', views.udel, name='udel'),
    url(r'^uedit/(?P<uid>[0-9]+)', views.uedit, name='uedit'),
    url(r'^uupdate/', views.uupdate, name='uupdate'),
    # 商品管理
    url(r'^goodslist/', viewsGoods.Goodlist, name='goodslist'),
    url(r'^typeadd/', viewsGoods.typeadd, name='typeadd'),
    url(r'^typeinsert/', viewsGoods.typeinsert, name='typeinsert'),
    url(r'^typelist/', viewsGoods.typelist, name='typelist'),
    url(r'^goodsadd/', viewsGoods.goodsadd, name='goodsadd'),
    url(r'^orderlist/', viewsGoods.orderlist, name='orderlist'),



]
