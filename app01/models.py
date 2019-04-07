from django.db import models

# Create your models here.

# 用户实体类
class User(models.Model):
    # 定义用户名为主键，最大长度不超过20
    uname = models.CharField(primary_key=True, max_length=20)
    # 定义用户密码，最大长度不超过20
    upwd = models.CharField(max_length=20)

# 商品实体类
class Goods(models.Model):
    # 商品编号，自动，主键
    gid = models.AutoField(primary_key=True)
    # 商品名称，最大长度不超过30
    gname = models.CharField(max_length=30)