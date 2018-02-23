from django.contrib import admin
from blogpost.models import Blogpost
# Register your models here.

class BlogpostAdmin(admin.ModelAdmin):
	"""docstring for ClassName"""
	exclude = ['posted']
	prepopulated_field = {'slug':('title',)}

admin.site.register(Blogpost,BlogpostAdmin)
		