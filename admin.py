from django.contrib import admin
from .models import User,audiofiles,compareaudiofiles


# Register your models here.
admin.site.register(User)
admin.site.register(audiofiles)
admin.site.register(compareaudiofiles)
