from django.contrib import admin
# Register your models here.
from .models import Name,Author,Book

admin.site.register(Name)
admin.site.register(Author)
admin.site.register(Book)