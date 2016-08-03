from django.contrib import admin
from .models import Article, images
# Register your models here.

class images_inline(admin.StackedInline):
	model = images
	extra = 5

class ArticleAdmin(admin.ModelAdmin):
	fieldsets = [
	(None, {'fields':['title']}),
	]
	inlines = [images_inline]

admin.site.register(Article, ArticleAdmin)