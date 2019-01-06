from django import forms
from django.core.files import File
from django.core.files.base import ContentFile

from PIL import Image
from io import BytesIO

from .models import Photo

class PhotoForm(forms.ModelForm):
	x = forms.FloatField(widget=forms.HiddenInput())
	y = forms.FloatField(widget=forms.HiddenInput())
	image_width = forms.FloatField(widget=forms.HiddenInput())
	image_height = forms.FloatField(widget=forms.HiddenInput())

	class Meta:
		model = Photo
		fields = ('title', 'image', 'x', 'y', 'image_height', 'image_width')

	def save(self, *args, **kwargs):
		photo = super(PhotoForm, self).save(commit=False)

		x = self.cleaned_data.get('x')
		y = self.cleaned_data.get('y')
		w = self.cleaned_data.get('image_width')
		h = self.cleaned_data.get('image_height')

		image = Image.open(photo.image)
		cropped_image = image.crop((x, y, w + x, h + y))
		resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
		thumb_io = BytesIO()
		print(resized_image.format)
		resized_image.save(thumb_io, format=image.format)
		photo.save(image.filename, ContentFile(thumb_io.getvalue(), f'{image.filename}'))

		return super(PhotoForm, self).save(*args, **kwargs)
