from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Author(models.Model):  
    full_name = models.CharField(max_length=100)  
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)
    test = models.CharField(max_length=100, null=True) 

    def __str__(self):
        return "{}, {}".format(self.full_name, self.birth_year)

class Book(models.Model):  
    ISBN = models.CharField(max_length=13)  
    title = models.TextField()  
    description = models.TextField()  
    year_release = models.SmallIntegerField()  
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True, related_name='books')

    def __str__(self):
        return self.title


