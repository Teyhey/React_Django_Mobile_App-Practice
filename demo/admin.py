from django.contrib import admin
from .models import Book

@admin.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'descriptions', 'price']
    list_filter = ['published']
    search_fields = ['title', 'descriptions']
    
