from django.contrib import admin

from .models import Category, Post, Comments

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    #prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Category)

@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('created_on', 'active')
    search_fields = ('body', 'name')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)