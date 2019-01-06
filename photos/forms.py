from PIL import Image
from django import forms
from django.core.files import File

from .models import Photo

class PhotoForm(forms.ModelForm):
	x = forms.FloatField(widget=forms.HiddenInput())
	y = forms.FloatField(widget=forms.HiddenInput())
	image_width = forms.FloatField(widget=forms.HiddenInput())
	image_height = forms.FloatField(widget=forms.HiddenInput())

	class Meta:
		model = Photo
		fields = ('title', 'image', 'x', 'y', 'image_height', 'image_width')

	def save(self):
		photo = super(PhotoForm, self).save(commit=False)

		x = self.cleaned_data.get('x')
		y = self.cleaned_data.get('y')
		w = self.cleaned_data.get('image_width')
		h = self.cleaned_data.get('image_height')

		image = Image.open(photo.image)
		cropped_image = image.crop((x, y, w + x, h + y))
		resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
		resized_image.save(photo.image.path)

		return super(PhotoForm, self).save(commit=True)
