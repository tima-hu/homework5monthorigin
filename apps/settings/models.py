from django.db import models

# Create your models here.

class Library(models.Model):
    title = models.CharField(
        max_length=144,
        verbose_name="Заголовок"
    )
    description= models.TextField(
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to="Settings",
        verbose_name="Фото"
    )
    
    def str(self):
        return self.title
    
class Meta:
    verbose_name = "Библеотека"
    verbose_name = "Библеотеки"

class Author(models.Model):
    name = models.CharField(max_length=155)
    birth_year = models.CharField(max_length=155)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = "Авторы"
class Book(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="author")
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = "Книги"