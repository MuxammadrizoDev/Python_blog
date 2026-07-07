from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='banners/')
    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='categories/')

    def __str__(self):
        return self.name


class Blogs(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blogs/')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


class Contacts(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class OurData(models.Model):
    work_time = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
