from django.db import models

# Create your models here.
class Home_user(models.Model):
	username = models.CharField(max_length=32)
	password = models.CharField(max_length= 60)


	class Meta:
		db_table = 'home_info'

	def __str__(self):
		return self.username

# class Users(models.Model):
# 	username = models.CharField(max_length=32, unique=True)
# 	name = models.CharField(max_length=16, null=True) 
# 	password = models.CharField(max_length= 80)
# 	sex = models.CharField(max_length=1, null=True)
# 	address = models.CharField(max_length=255, null=True)
# 	code = models.CharField(max_length=6, null=True)
# 	phone = models.CharField(max_length=16, null=True)
# 	email = models.CharField(max_length=50)
# 	state = models.IntegerField(null=True)
# 	img = models.ImageField(upload_to='static/public/img')
# 	addtime = models.DateField(auto_now_add=True)
	