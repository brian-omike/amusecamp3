from django.db import models

# Create your models here.
class Image(models.Model):
	caption = models.CharField(max_length=50)
	image = models.ImageField(upload_to="images/")

	def __str__(self):
		return self.caption

class Gallery(models.Model):
	description = models.CharField(max_length=50)
	photo = models.ImageField(upload_to="images/")

	def __str__(self):
		return self.description

class Lost(models.Model):
	item = models.CharField(max_length=50)

	def __str__(self):
		return self.item
