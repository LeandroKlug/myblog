from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publicado', 'status')
    list_filter = ('status', 'criado', 'publicado', 'author')
    raw_id_fields = ('author',)
    date_hierarchy = 'publicado'
    search_fields = ('title', 'context')
    prepopulated_fields = {'slug': ('title',)}


