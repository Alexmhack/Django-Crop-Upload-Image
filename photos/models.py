from django.db import models

class Photo(models.Model):
	title = models.CharField(max_length=144)
	image_heigth = models.IntegerField()
	image_width = models.IntegerField()
	image = models.ImageField(
		upload_to='media/%Y/%m/%d/',
		height_field=image_heigth,
		width_field=image_width
	)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.title)
