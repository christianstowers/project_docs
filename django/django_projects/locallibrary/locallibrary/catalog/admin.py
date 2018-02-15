from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
admin.site.register(Language)

#Define the admin class
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

#Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

'''
use the @register decorator to register the models 
(this does exactly the same thing as the admin.site.register() syntax)
'''

#Register the Admin classes for Book using the decorator '@'
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'display_genre', 'language')
'''
from mdn article:
Unfortunately we can't directly specify the genre field in 
list_display because it is a ManyToManyField (Django prevents 
this because there would be a large database access "cost" 
in doing so). Instead we'll define a display_genre function to 
get the information as a string 
'''
#Register the Admin classes for BookInstance using the decorator '@' as well
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
	list_filter = ('status', 'due_back')


