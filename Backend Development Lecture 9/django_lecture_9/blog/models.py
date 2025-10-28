from django.db import models

class Blog(models.Model):
    title = models.CharField(verbose_name="სათაური", max_length=255)
    text = models.TextField(verbose_name="ტექსტი" )
    active =  models.BooleanField(verbose_name="აქტიურია", default=True)
    create_date = models.DateTimeField(verbose_name="შექმნით დრო", auto_now_add=True, null=True)
    update_date = models.DateTimeField(verbose_name="განახლების დრო", auto_now=True, null=True)
    email = models.EmailField (verbose_name="იმეილი",  unique=True, null=True)
    website = models.URLField (verbose_name="ვებსაიტი", null=True)

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