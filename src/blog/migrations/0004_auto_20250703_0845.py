# Generated by Django 2.2.18 on 2025-07-03 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, default='static/images/img.png', null=True, upload_to='uploads/', verbose_name='封面图片'),
        ),
    ]
