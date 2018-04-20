from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import Types,Goods,Users,Order,OrderInfo
import os,time
from django.conf import settings
# Create your views here.


def gettypeall():
     # 查询导航分类信息 查询所有的二级分类
    l = Types.objects.exclude(pid=0)
    return l

def index(request):

    # 查询所有顶级分类
    t = Types.objects.filter(pid=0)

    arr = []
    for v in t:
        v.sub = Types.objects.filter(pid = v.id)
        for x in v.sub:
            x.sub = Goods.objects.filter(typeid_id = x.id)
        arr.append(v)


    # arr = [
    #     {'name':'服装','sub':[{'name':'男装','sub':[{}]},{'name':'女装','sub':[{},{}]}]},
    #     {'name':'数码','sub':[{'name':'手机'}]}
    # ]


    # print(arr[0].sub[0].sub[0].title)


    # 分配数据
    context = {'typelist':gettypeall(),'typegoods':arr}

    return render(request,'home/index.html',context)



def lists(request,tid):
    # 查询当前的分类
    t = Types.objects.get(id=tid)

    # print(t) # Types.objects.filter(id=tid) <QuerySet [<Types: 服装>]> [{}]
    # print(t) # Types.objects.get(id=tid) Types object  {}

    # 判断当前分类是否为一级分类
    if t.pid == 0:
        # 如果是一级分类,则再查询当前分类下的子类
        t.sub = Types.objects.filter(pid=tid)
        # 再查询子类下的商品信息
        for v in t.sub:
            v.sub = Goods.objects.filter(typeid_id=v.id)
    else:
        # 二级分类
        # 查询当前分类下的商品
        t.sub = Goods.objects.filter(typeid_id=t.id)
        # 查询当前分类下的父类信息
        t.pname = Types.objects.get(id=t.pid)
        # 查询当前分类的同级信息 ,查询pid和我的pid一样的分类信息,并排除我自己
        t.siblings = Types.objects.filter(pid=t.pid).exclude(id=t.id)



        # 一级分类
        # {
        #     'name':'服装',
        #     'sub':[
        #           {'name':'男装','sub':[{},{}]},
        #           {'name':'女装','sub':[{},{}]}
        #         ]
        # }


        # 二级分类
        # {
        #     'name':'男装',
        #     'sub':[{},{}],
        #     'pname':{'name':'服装',id:1},
        #     'siblings':[{'name':'女装'}]
        # }


    # 判断当前是否有pname属性
    # if hasattr(t,'pname'):
    #     # 如果有pname 证明时二级类
    #     print(t.pname.name)
    #     print('二级类')
    # else:
    #     # 如果没有pname 证明时一级类
    #     print(t.name)
    #     print('一级类')


    # 分配数据
    context = {'typelist':gettypeall(),'lists':t}
    
    return render(request,'home/lists.html',context)




def goods(request,gid):

    # 根据id查询商品信息
    ob = Goods.objects.get(id=gid)


    # 分配数据
    context = {'typelist':gettypeall(),'ginfo':ob}
    
    return render(request,'home/goods.html',context)



def cartadd(request):
    
    # 接受参数 商品id,购买数量
    gid = request.POST['gid']
    num = int(request.POST['num'])

    # 获取session中的购物车
    data = request.session.get('cart',{})

    # 判断是否有商品已经存在于购物车中
    if gid in data.keys():
        # 如果商品已经存在于购物车中,只修改数量
        data[gid]['num'] += num
    else:
        # 如果不存在,则查询数据,添加到购物车中
        # 获取商品对象
        goods = Goods.objects.get(id=gid)
        # 组装数据
        arr = {'title':goods.title,'id':goods.id,'price':float(goods.price),'pic':goods.pic,'num':num}
        data[gid] = arr

    
    # 存入session购物车中
    request.session['cart'] = data

    # return HttpResponse('ok')

    return HttpResponse('<script>alert("添加成功");location.href="/cartindex/"</script>')
    ''' 
        data=
        {
            6: {'id': 6, 'price': 99.9, 'pic': '/static/public/img/1523839869.9352133.jpg', 'num': '1', 'title': '红虎皮超短裙,配黑丝袜'}, 
            5: {'id': 5, 'price': 199.8, 'pic': '/static/public/img/1523839666.313034.jpg', 'title': '倜傥风流的大鼻涕 风衣', 'num': '1'}
        }
    '''
    

# 购物车列表页
def cartindex(request):
    # 获取购物车信息
    cart = request.session.get('cart',{})

   

    context = {'cart':cart,'typelist':gettypeall()}

    return render(request,'home/cart.html',context)
    # return HttpResponse('cartindex')

# 清空购物车
def cartclear(request):
    
    request.session['cart'] = {}

    return HttpResponse('cartclear')


# def cartdel(request,gid):
#     # 获取购物车信息
#     cart = request.session.get('cart',{})

#     del cart['6']

#     request.session['cart'] = cart

# 修改购物车商品数量
def cartedit(request):

    gid = request.GET.get('gid',None)
    num = request.GET.get('num',None)

    # 获取购物车信息
    cart = request.session.get('cart',{})
    # 修改对应商品的数量
    cart[gid]['num'] = int(num)
    # 把修改后的数据存入session
    request.session['cart'] = cart

    # return HttpResponse('<script>location.href="/cartindex/"</script>')
    return HttpResponse('0')


# 订单确认
def orderadd(request):
    # 选择购买的商品id
    ids = request.POST.get('ids','').split(',')
    # # 购物车数据{6:{},5:{}}
    cart = request.session['cart']

    # 组装已购买的商品数据
    order = []
    for x in ids:
        order.append(cart[x])

    context = {'orders':order,'ids':ids}



    return render(request,'home/ordercofim.html',context)

# 生成订单
def ordercreate(request):


  

    # 购买的商品id [1,2,4]
    ids = request.POST.get('ids','').split(',')
    # {1:{},2:{},4:{}}
    cart = request.session['cart']
    totalprice = 0
    totalnum = 0

    for x in ids:
        totalprice += (cart[x]['price'] * cart[x]['num'])
        totalnum += cart[x]['num']

    # 先去添加订单信息
    od = Order()
    od.uid = Users.objects.get(id=request.session['VipUser']['uid'])
    # 收货信息 
    od.addname = request.POST['addname']
    od.address = request.POST['address']
    od.addphone = request.POST['addphone']
    od.addcode = request.POST['addcode']
    # 总价
    od.totalprice = totalprice
    # 总数
    od.totalnum = totalnum
    # 状态
    od.status = 1

    od.save()

    # 再去添加订单详情信息
    for x in ids:
        info = OrderInfo()
        info.orderid = od
        info.gid = Goods.objects.get(id=x)
        info.num = cart[x]['num']
        info.price = cart[x]['price']
        info.save()
        # 购物车中对应的商品信息
        del cart[x]

    # 把购物车信息重新存入session中
    request.session['cart'] = cart


    # 跳转到付款页面
    return HttpResponse('<script>alert("下蛋成功");location.href="/buy/'+str(od.id)+'"</script>')



# 付款
def buy(request,oid):
    # 根据oid查询订单信息,展示付款页面
    ob = Order.objects.get(id=oid)

    context = {'order':ob}
    
    # return HttpResponse('buy')
    return render(request,'home/buy.html',context)

# 支付
def pay(request,oid):
    # 根据oid查询订单信息,展示付款页面
    ob = Order.objects.get(id=oid)

    ob.status = 2
    
    return HttpResponse('<script>alert("付款成功");location.href="/myorder/"</script>')


# 我的订单
def myorder(request):
    
    # 获取用户id
    uid = request.session['VipUser']['uid']
    # 查询用户的订单
    ob = Order.objects.filter(uid=uid)

    # filter 查询集 [{info:[{},{}]},{}]
    for x in ob:
        x.info = x.orderinfo_set.all()
    
    # print(ob[0].info[0].gid.title)


    return render(request,'home/myorder.html',{'orders':ob})


# 登录视图
def login(request):
    if request.method == 'GET':
        return render(request,'home/login.html')
    else:
        try:
            # 接收用户名和密码,检测是否正确
            ob = Users.objects.get(username=request.POST['username'])

            if ob.status != 2:
                # 检测密码是否正确
                from django.contrib.auth.hashers import check_password
                # 验证密码
                res = check_password(request.POST['password'],ob.password)
                # 判断密码是否正确
                if res:
                    # 登录成功,用户信息.,记录到session,跳转地址
                    request.session['VipUser'] = {'uid':ob.id,'username':ob.username,'pic':ob.pic}
                    return HttpResponse('<script>alert("登录成功");location.href="/"</script>')
                else:
                    # 密码错误
                    raise

        except:
            pass
            
        return HttpResponse('<script>alert("用户名或密码错误");location.href="/login/"</script>')
