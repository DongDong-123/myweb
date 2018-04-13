from django.db import models 


class Users(models.Model):
	username = models.CharField(max_length=32, unique=True)
	name = models.CharField(max_length=16, null=True) 
	password = models.CharField(max_length= 80)
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


class Types(models.Model):	
	name = models.CharField(max_length=32)
	pid = models.IntegerField(default=0)
	path = models.CharField(max_length=255)
	

class Goods(models.Model):
	typeid = models.ForeignKey(to='Types', to_field='id')
	goods = models.CharField(max_length=32)
	company = models.CharField(max_length=50, null=True)
	descr = models.TextField(null=True)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	picname = models.CharField(max_length=255, null=True)
	state = models.IntegerField(default=1)
	store = models.IntegerField(default=0)
	clicknum = models.IntegerField(default=0, null=True)
	addtime = models.DateTimeField(auto_now_add=True)


class Orders(models.Model):
	uid = models.IntegerField()
	linkman = models.CharField(max_length=32)
	address = models.CharField(max_length=255)
	code = models.CharField(max_length=6)
	phone = models.CharField(max_length=16)
	addtime = models.IntegerField()
	total = models.DecimalField(max_digits=8, decimal_places=2)
	status = models.IntegerField(default=0)


class Detail(models.Model):
	orderid = models.OneToOneField(Orders)
	goodsid = models.IntegerField()
	name = models.CharField(max_length=32)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	num = models.IntegerField()
