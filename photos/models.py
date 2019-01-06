from django.db import models
from django.urls import reverse

from image_cropping import ImageRatioField

class Photo(models.Model):
	title = models.CharField(max_length=144)
	image = models.ImageField(
		upload_to='%Y/%m/%d/',
		height_field='image_heigth',
		width_field='image_width'
	)
	cropping = ImageRatioField('image', '250x250')
	image_heigth = models.IntegerField()
	image_width = models.IntegerField()
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.title)

	def get_absolute_url(self):
		return reverse("photos:detail")
