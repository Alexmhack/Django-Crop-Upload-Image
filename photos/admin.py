from django.contrib import admin

from image_cropping import ImageCroppingMixin

from .models import Photo

class PhotoModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
	pass


admin.site.register(Photo, PhotoModelAdmin)
