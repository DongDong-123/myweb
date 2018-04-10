from django.db import models

# Create your models here.
class Home_user(models.Model):
	username = models.CharField(max_length=32)
	password = models.CharField(max_length= 60)


	class Meta:
		db_table = 'home_info'

	def __str__(self):
		return self.username