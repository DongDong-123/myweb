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

    url(r'^user/index', views.index, name='index'),
    # 注册登录
    url(r'^user/regedit$', views.regedit, name='regedit'),
    url(r'^user/checkregedit', views.checkregedit, name='checkregedit'),
    url(r'^user/insertregedit', views.insertregedit, name='insertregedit'),
    url(r'^user/login', views.login, name='login'),
    # url(r'^user/checkname', views.checkname, name='checkname'),
    # 商品列表
    url(r'^user/goodslist/(?P<tid>[0-9]+)/(?P<tpid>[0-9]+)', views.goodslist, name='list'),
    # url(r'^user/index', views.index, name='index'),
    # 商品详情
    url(r'^user/goods/(?P<tid>[0-9]+)', views.goods, name='goods'),
    # 购物车
    url(r'^user/cartindex', views.cartindex, name='cartindex'),
    url(r'^user/cartadd', views.cartadd, name='cartadd'),
    url(r'^user/cartdel/(?P<tid>[0-9]+)', views.cartdel, name='cartdel'),



]
