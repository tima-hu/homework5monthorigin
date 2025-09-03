from django.db import models
from django.contrib.auth.models import User

class Library(models.Model):
    title = models.CharField(max_length=144, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="Settings", verbose_name="Фото")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Библиотека"
        verbose_name_plural = "Библиотеки"


class Author(models.Model):
    name = models.CharField(max_length=155)
    birth_year = models.CharField(max_length=155)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Book(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    library = models.ForeignKey(
        Library,
        on_delete=models.CASCADE,
        related_name='books',
        null=True,  # обязательно, если уже есть записи
        blank=True)
    published_year = models.CharField(max_length=4)
    genre = models.CharField(max_length=155, verbose_name="Жанр", blank=True, null=True)
    pages = models.CharField(max_length=4, verbose_name="Количество страниц", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True) 

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ['-created_at']


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='bookings')
    booked_at = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)  # дата возврата
    is_active = models.BooleanField(default=True)  # активное бронирование

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"

    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"
        ordering = ['-booked_at']

class Reader(models.Model):
    user = models.CharField(max_length=150, verbose_name="Имя пользователя")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"

class Borrowing(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.SET_NULL, related_name='borrowings', null=True)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, related_name='borrowings', null=True)
    borrowed_at = models.DateTimeField(auto_now_add=True,verbose_name="Дата заимствования")
    return_date = models.DateTimeField(verbose_name="Дата возврата")
    returned = models.BooleanField(default=False, verbose_name="Возвращено")

    def save(self, *args, **kwargs):
        if not self.pk:
            if self.book.available_copies <= 0:
                raise ValueError("Нет доступных копий книги")
            self.book.available_copies -= 1
            self.book.save()
            self.save()

    def mark_as_returned(self):
        if not self.returned:
            self.returned = True
            self.book.available_copies += 1
            self.book.save()
            self.save()
    def __str__(self):
        return f"{self.reader.user.username} - {self.book.title}"

    class Meta:
        verbose_name = "Заимствование"
        verbose_name_plural = "Заимствования"
        ordering = ['-borrowed_at']