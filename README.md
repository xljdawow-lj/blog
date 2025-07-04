## Django搭建博客
![py35](https://img.shields.io/badge/Python-3.5-red.svg) 
![Django2.2](https://img.shields.io/badge/Django-2.2.0-green.svg)
[![](https://img.shields.io/badge/Powered%20by-@j_hao104-blue.svg)](http://www.spiderpy.cn/blog/)

使用Django快速搭建博客
### 要求
* Python: 3.5
* Django: 2.2.0

### 下载
```
wget https://github.com/xljdawow-lj/blog/archive/master.zip
or
git clone git@github.com:xljdawow-lj/blog.git
```

### 安装
```
pip install -r requirements.txt  # 安装所有依赖
修改setting.py配置数据库
配置畅言：到http://changyan.kuaizhan.com/注册站点,将templates/blog/component/changyan.html中js部分换成你在畅言中生成的js。
畅言js位置: 畅言管理后台-》安装畅言-》通用代码安装-》自适应安装代码
python manage.py makemigrations blog
python manage.py migrate
python manage.py runserver
```
[文档](docs/install.md)

### 使用

```python
# 初始化用户名密码
python manage.py createsuperuser
# 按照提示输入用户名、邮箱、密码即可
# 登录后台 编辑类型、标签、发布文章等
http://ip:port/admin

```

浏览器中打开<http://127.0.0.1:8000/>即可访问

## Screen Shots

* 首页
![首页](docs/image/img_1.png)

* 文章列表
![文章列表](docs/image/img_2.png)

* 文章内容
![文章内容](docs/image/img_3.png)
