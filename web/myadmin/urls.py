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
from . import views, viewsGoods, viewsTypes, viewsOrder

urlpatterns = [
    # url(r'^calendar/', views.calendar, name='calendar'),
    # url(r'^chart/', views.chart, name='chart'),
    # url(r'^form/', views.form, name='form'),
    # url(r'^login/', views.login, name='login'),
    # url(r'^sign_up/', views.sign_up,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   name='sign_up'),
    # url(r'^tables/', views.tables, name='tables'),
    url(r'^table_list_img/', views.table_list_img, name='table_list_img'),
    url(r'^table_list/', views.table_list, name='table_list'),
    # 用户管理
    url(r'^myadmin/', views.myadmin, name='myadmin'),
    url(r'^uadd/', views.uadd, name='uadd'),
    url(r'^insert/', views.insert, name='insert'),
    url(r'^ulist/', views.ulist, name='ulist'),
    url(r'^udel/(?P<uid>[0-9]+)', views.udel, name='udel'),
    url(r'^uedit/(?P<uid>[0-9]+)', views.uedit, name='uedit'),
    url(r'^uupdate/', views.uupdate, name='uupdate'),
    # 分类管理
    url(r'^typeadd/', viewsTypes.typeadd, name='typeadd'),
    url(r'^typeinsert/', viewsTypes.typeinsert, name='typeinsert'),
    url(r'^typeedit/(?P<tid>[0-9]+)', viewsTypes.typeedit, name='typeedit'),
    url(r'^typedel/(?P<tid>[0-9]+)', viewsTypes.typedel, name='typedel'),
    url(r'^typelist/', viewsTypes.typelist, name='typelist'),
    url(r'^typeupdate/', viewsTypes.typeupdate, name='typeupdate'),
    # 商品管理
    url(r'^goodslist/', viewsGoods.Goodslist, name='goodslist'),
    url(r'^goodsadd/', viewsGoods.Goodsadd, name='goodsadd'),
    url(r'^goodsinsert/', viewsGoods.Goodsinsert, name='goodsinsert'),
    url(r'^goodsedit/', viewsGoods.Goodsedit, name='goodsedit'),
    url(r'^goodsdel/(?P<gid>[0-9]+)', viewsGoods.Goodsdel, name='goodsdel'),
    url(r'^goodsupdate/', viewsGoods.Goodsupdate, name='goodsupdate'),
    # 订单管理
    url(r'^orderlist/', viewsOrder.orderlist, name='orderlist'),
    # url(r'^orderlist/', viewsOrder.orderlist, name='orderlist'),
    # url(r'^orderlist/', viewsOrder.orderlist, name='orderlist'),
    # url(r'^orderlist/', viewsOrder.orderlist, name='orderlist'),
    # url(r'^orderlist/', viewsOrder.orderlist, name='orderlist'),



]
