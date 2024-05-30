from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=225)
    image = models.FileField(upload_to='uploads/',blank=True,null=True,default='')
    content = models.TextField()
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    