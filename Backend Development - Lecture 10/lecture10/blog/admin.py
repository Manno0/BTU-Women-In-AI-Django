from django.contrib import admin
from .models import Blog
from .models import BlogImages
from .models import Author


admin.site.register(Blog)
admin.site.register(BlogImages)
admin.site.register(Author)

# Register your models here.
