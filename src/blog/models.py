from django.db import models
from django.conf import settings


# Create your models here.

class Tag(models.Model):
    tag_name = models.CharField('标签名称', max_length=30)

    def __str__(self):
        return self.tag_name

from ckeditor.fields import RichTextField

class Article(models.Model):
    objects = None
    title = models.CharField(max_length=200)  # 博客标题
    category = models.ForeignKey('Category', verbose_name='文章类型', on_delete=models.CASCADE)
    date_time = models.DateField(auto_now_add=True)  # 博客日期
    # content = models.TextField(blank=True, null=True)  # 文章正文
    content = RichTextField(blank=True, null=True)  # 替换原来的TextField
    digest = models.TextField(blank=True, null=True)  # 文章摘要
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者', on_delete=models.CASCADE)
    view = models.BigIntegerField(default=0)  # 阅读数
    comment = models.BigIntegerField(default=0)  # 评论数
    # picture = models.CharField(max_length=200)  # 标题图片地址
    # 图片字段（非必填，无上传时自动使用 media/default.jpg）
    # picture = models.ImageField(
    #     upload_to='uploads/',         # 上传目录
    #     blank=True,                   # 非必填
    #     null=True,                    # 数据库允许NULL
    #     default='static/images/img.png',        # 直接指定默认图片名
    #     verbose_name="封面图片"
    # )
    tag = models.ManyToManyField(Tag)  # 标签

    def __str__(self):
        return self.title

    def sourceUrl(self):
        source_url = settings.HOST + '/blog/detail/{id}'.format(id=self.pk)
        return source_url  # 给网易云跟帖使用

    def viewed(self):
        """
        增加阅读数
        :return:
        """
        self.view += 1
        self.save(update_fields=['view'])

    def commenced(self):
        """
        增加评论数
        :return:
        """
        self.comment += 1
        self.save(update_fields=['comment'])

    class Meta:  # 按时间降序
        ordering = ['-date_time']


class Category(models.Model):
    object=None
    name = models.CharField('文章类型', max_length=30)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_mod_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = "文章类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Comment(models.Model):
    object=None
    title = models.CharField("标题", max_length=100)
    source_id = models.CharField('文章id或source名称', max_length=25)
    create_time = models.DateTimeField('评论时间', auto_now=True)
    user_name = models.CharField('评论用户', max_length=25)
    url = models.CharField('链接', max_length=100)
    comment = models.CharField('评论内容', max_length=500)
