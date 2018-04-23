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
    # 首页
    url(r'^myadmin/$', views.myadmin, name='myadmin'),
    # 用户管理
    url(r'^myadmin/uadd/', views.uadd, name='uadd'),
    url(r'^myadmin/insert/', views.insert, name='insert'),
    url(r'^myadmin/ulist/', views.ulist, name='ulist'),
    url(r'^myadmin/udel/(?P<uid>[0-9]+)', views.udel, name='udel'),
    url(r'^myadmin/uedit/(?P<uid>[0-9]+)', views.uedit, name='uedit'),
    url(r'^myadmin/uupdate/', views.uupdate, name='uupdate'),
    # 分类管理
    url(r'^myadmin/typeadd/', viewsTypes.typeadd, name='typeadd'),
    url(r'^myadmin/typeinsert/', viewsTypes.typeinsert, name='typeinsert'),
    url(r'^myadmin/typeedit/(?P<tid>[0-9]+)', viewsTypes.typeedit, name='typeedit'),
    url(r'^myadmin/typedel/(?P<tid>[0-9]+)', viewsTypes.typedel, name='typedel'),
    url(r'^myadmin/typelist/', viewsTypes.typelist, name='typelist'),
    url(r'^myadmin/typeupdate/', viewsTypes.typeupdate, name='typeupdate'),
    # 商品管理
    url(r'^myadmin/goodslist/', viewsGoods.Goodslist, name='goodslist'),
    url(r'^myadmin/goodsadd/', viewsGoods.Goodsadd, name='goodsadd'),
    url(r'^myadmin/goodsinsert/', viewsGoods.Goodsinsert, name='goodsinsert'),
    url(r'^myadmin/goodsedit/(?P<gid>[0-9]+)', viewsGoods.Goodsedit, name='goodsedit'),
    url(r'^myadmin/goodsdel/(?P<gid>[0-9]+)', viewsGoods.Goodsdel, name='goodsdel'),
    url(r'^myadmin/goodsupdate/', viewsGoods.Goodsupdate, name='goodsupdate'),
    # 订单管理
    url(r'^myadmin/orderlist/', viewsOrder.Orderlist, name='orderlist'),
    url(r'^myadmin/orderedit//(?P<tid>[0-9]+)', viewsOrder.Orderedit, name='orderedit'),
    url(r'^myadmin/orderupdate/', viewsOrder.Orderupdate, name='orderupdate'),
    # 后台登录
    url(r'^myadmin/login', views.login, name='adminlogin'),
    url(r'^myadmin/dologin', views.dologin, name='admindologin'),
    url(r'^myadmin/logout', views.logout, name='adminlogout'),
    url(r'^myadmin/verifycode', views.verifycode, name='vcode'),

]
