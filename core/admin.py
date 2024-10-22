from os import path
from django.contrib import admin

from core.models import Tag, Video


class VideoAdmin(admin.ModelAdmin):
  def get_urls(self):
    urls = super().get_urls()
    custom_urls = [
      path('<int:id>/upload-video', self.upload_video, name='core_video_create'),
    ]
    
    return custom_urls + urls
  def upload_video(self, request, id):
    pass

admin.site.register(Video)
admin.site.register(Tag)
