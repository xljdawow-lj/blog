from __future__ import unicode_literals

from django.apps import AppConfig

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'  # 必须与应用目录名一致
