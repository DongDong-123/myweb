from django.db import models

# Create your models here.
class Users(models.Model):
	username = models.CharField(max_length=32, unique=True)
	name = models.CharField(max_length=16, null=True)
	password = models.CharField(max_length= 32)
	sex = models.IntegerField(max_length=1, null=True)
	address = models.CharField(max_length=255, null=True)
	code = models.CharField(max_length=6, null=True)
	phone = models.CharField(max_length=16, null=True)
	email = models.CharField(max_length=50)
	state = models.IntegerField(max_length=1, null=True)
	addtime = models.IntegerField(null=True)

	# class Meta:
	# 	db_table = 'userinfo'

	def __str__(self):
		return self.username

class Type(models.Model):
	name = models.CharField(max_length=32)
	pid = models.IntegerField(default=0)
	path = models.CharField(max_length=255)

	# class Meta:
	# 	db_table = 'userinfo'

	# def __str__(self):
	# 	return self.name

class Goods(models.Model):
	typeid = models.IntegerField()
	goods = models.CharField(max_length=32)
	company = models.CharField(max_length=50)
	descr = models.TextField()
	price = models.DecimalField(max_digits=6, decimal_places=2)
	picname = models.CharField(max_length=255)
	state = models.IntegerField(max_length=1, default=1)
	store = models.IntegerField(default=0)
	num = models.IntegerField(default=0)
	clicknum = models.IntegerField(default=0)
	addtime = models.IntegerField()




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
