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
from . import views

urlpatterns = [
    # 首页
    url(r'^$',views.index,name="index"),
    # 列表
    url(r'^lists/(?P<tid>[0-9]+)$',views.lists,name="lists"),
    # 详情
    url(r'^goods/(?P<gid>[0-9]+)$',views.goods,name="goods"),

    # 登录
    url(r'^login/$',views.login,name="login"),


    # 购物车
    # 加入购物车
    url(r'^cartadd/$',views.cartadd,name="cartadd"),
    # 购物车列表
    url(r'^cartindex/$',views.cartindex,name="cartindex"),
    # 清空购物车
    url(r'^cartclear/$',views.cartclear,name="cartclear"),
    # 修改购物车数量
    url(r'^cartedit/$',views.cartedit,name="cartedit"),


    # 需要登录
    # 提交订单,确认订单信息
    url(r'^orderadd/$',views.orderadd,name="orderadd"),
    # 生成订单
    url(r'^ordercreate/$',views.ordercreate,name="ordercreate"),
    # 付款页面
    url(r'^buy/(?P<oid>[0-9]+)$',views.buy,name="buy"),
    # 支付
    url(r'^pay/(?P<oid>[0-9]+)$',views.pay,name="pay"),

    # 我的订单
    url(r'^myorder/$',views.myorder,name="myorder"),


]