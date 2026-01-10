from django.contrib.auth.forms import AuthenticationForm
from django.db import models

class Blog(models.Model):
    title= models.CharField(verbose_name= "სათაური",max_length=200)
    text= models.TextField(verbose_name = "ტექსტი")
    active = models.BooleanField(default= True, verbose_name= "აქტიური")
    created_at=models.DateTimeField(verbose_name="შექმნის თარიღი",  auto_now_add= True, null= True, blank= True)
    updated_at=models.DateTimeField(verbose_name="განახლების თარიღი",auto_now= True, null= True, blank= True)
    email=models.EmailField(verbose_name="იმეილი", unique= True, null= True)
    website=models.URLField(verbose_name="ვებსაიტი", unique= True, null= True)
    documents=models.FileField(upload_to="files/", null= True, blank= True)
    authors=models.ManyToManyField(to="Author",verbose_name="ავტორები",related_name="authors")



    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        ordering = ["title"]

    def __str__(self):
        return self.title

class Author(models.Model):
    first_name=models.CharField(verbose_name="სახელი",  max_length=200)
    last_name=models.CharField(verbose_name="გვარი",max_length=200)
    email=models.EmailField(verbose_name="მეილი", unique= True, null= True)
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        ordering = ["last_name"]
    def __str__(self)  :
        return f'{self.first_name} {self.last_name}'


class BlogImages(models.Model):
    image = models.ImageField(upload_to="images/", null= True, blank= True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "BlogImage"
        verbose_name_plural = "BlogImages"
        ordering = ["blog"]

    def __str__(self):
        return f'{self.blog.title} - {self.image}'

class BaseClass(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True



