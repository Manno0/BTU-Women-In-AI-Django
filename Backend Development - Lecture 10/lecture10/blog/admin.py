from django.contrib import admin
from .models import Blog
from .models import BlogImages

admin.site.register(Blog)
admin.site.register(BlogImages)

# Register your models here.
