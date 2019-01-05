from PIL import Image
from django import forms
from django.core.files import File

from .models import Photo

class PhotoForm(forms.ModelForm):
	class Meta:
		model = Photo
		fields = ('title', 'image')

	def save(self):
		photo = super().save()
		width = self.cleaned_data.get('image_width')
		heigth = self.cleaned_data.get('image_heigth')
		print(width, heigth)
		return photo
