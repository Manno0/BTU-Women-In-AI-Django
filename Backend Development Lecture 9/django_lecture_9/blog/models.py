from django.db import models

class Blog(models.Model):
    title = models.CharField(verbose_name="სათაური", max_length=255)
    text = models.TextField(verbose_name="ტექსტი" )

    class Meta:
        verbose_name = "blog"
        verbose_name_plural = "blogs"

    def __str__(self):
        return self.title