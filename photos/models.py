from django.db import models
from django.urls import reverse

class Photo(models.Model):
	title = models.CharField(max_length=144)
	image = models.ImageField(
		upload_to='%Y/%m/%d/',
		height_field='image_height',
		width_field='image_width'
	)
	image_height = models.FloatField()
	image_width = models.FloatField()
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.title)

	def get_absolute_url(self):
		return reverse("photos:detail")
