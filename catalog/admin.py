from django.contrib import admin

from .models import Book, Author, Publisher, Category

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','publisher','publication_date', 'is_available',)
    list_filter = ('is_available','publication_date','publisher', 'categories',)
search_fields = ('title',)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Category)
