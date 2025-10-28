from django.db import models

class Blog(models.Model):
    title = models.CharField(verbose_name="სათაური", max_length=255)
    text = models.TextField(verbose_name="ტექსტი" )
    active =  models.BooleanField(verbose_name="აქტიურია", default=True)

    class Meta:
        verbose_name = "blog"
        verbose_name_plural = "blogs"
        ordering = ['title']
        unique_together = ('title', 'text')

    def __str__(self):
        return self.title

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True