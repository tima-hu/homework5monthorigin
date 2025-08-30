from django.contrib import admin
from apps.settings.models import Library,Author,Book
# Register your models here.

admin.site.register(Library)
admin.site.register(Author)
admin.site.register(Book)