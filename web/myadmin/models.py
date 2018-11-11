from django.db import models


# 用户
class Users(models.Model):
    username = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=16, null=True)
    password = models.CharField(max_length=80)
    sex = models.CharField(max_length=1, null=True)
    address = models.CharField(max_length=255, null=True)
    code = models.CharField(max_length=6, null=True)
    phone = models.CharField(max_length=16, null=True)
    email = models.CharField(max_length=50)
    state = models.IntegerField(null=True)
    img = models.ImageField(upload_to='static/public/img')
    addtime = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username


# 分类
class Types(models.Model):
    name = models.CharField(max_length=32)
    pid = models.IntegerField(default=0)
    path = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# 商品
class Goods(models.Model):
    typeid = models.ForeignKey(to='Types', to_field='id', on_delete=models.CASCADE)
    goods = models.CharField(max_length=32)
    company = models.CharField(max_length=50, null=True)
    descr = models.TextField(null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    picname = models.CharField(max_length=255, null=True)
    state = models.IntegerField(default=1)
    store = models.IntegerField(default=0)
    clicknum = models.IntegerField(default=0, null=True)
    addtime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.goods


# 订单
class Orders(models.Model):
    uid = models.ForeignKey('Users', to_field="id", on_delete=models.CASCADE)
    linkman = models.CharField(max_length=32)
    address = models.CharField(max_length=255)
    code = models.CharField(max_length=6)
    phone = models.CharField(max_length=16)
    addtime = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    nums = models.IntegerField(default=1)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.linkman


# 订单详情
class Detail(models.Model):
    orderid = models.OneToOneField(Orders, on_delete=models.CASCADE)
    goodsid = models.ForeignKey('Goods', to_field="id", on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    num = models.IntegerField()

    def __str__(self):
        return self.name


# 轮播图控制
class Turnimg(models.Model):
    img = models.ImageField(upload_to='static/public/front/public/img')
