from django.contrib import admin

# Register your models here.


from blog.models import Tag, Article, Category


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_time'
    list_display = ('title', 'category', 'author', 'date_time', 'view')
    list_filter = ('category', 'author')
    filter_horizontal = ('tag',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

from django.contrib.auth.models import Group, User

# 隐藏 Django 后台的认证和授权（也就是说，隐藏后台账号添加和修改）
# admin.site.unregister(Group)
# admin.site.unregister(User)
