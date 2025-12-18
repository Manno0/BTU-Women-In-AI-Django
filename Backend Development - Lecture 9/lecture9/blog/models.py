from django.db import models

class BlogPost(models.Model):
    title= models.CharField(verbose_name= "სათაური",max_length=200)
    text= models.TextField(verbose_name = "ტექსტი")
    active = models.BooleanField(default= True, verbose_name= "აქტიური")
    created_at=models.DateTimeField(verbose_name="შექმნის თარიღი",  auto_now_add= True, null= True, blank= True)
    updated_at=models.DateTimeField(verbose_name="განახლების თარიღი",auto_now= True, null= True, blank= True)
    email=models.EmailField(verbose_name="იმეილი", unique= True, null= True)
    website=models.URLField(verbose_name="ვებსაიტი", unique= True, null= True)
    images=models.ImageField(upload_to="images/", null= True, blank= True)
    documents=models.FileField(upload_to="files/", null= True, blank= True)



    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ["title"]

    def __str__(self):
        return self.title

class BaseClass(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True



