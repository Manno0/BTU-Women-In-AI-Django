from django.contrib import admin
from .models import Blog
from .models import BlogImages
from .models import Author
from .models import BannerImages

admin.site.register(Blog)
admin.site.register(BlogImages)
admin.site.register(Author)
admin.site.register(BannerImages)

# Register your models here.
