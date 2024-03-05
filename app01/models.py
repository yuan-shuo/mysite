from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()

    # 要想给表新增一列数据，写法和上列一样，但是需要指定默认值或将其定义为空
    # 注意：在这里设置默认值只会补全前面没有的title数据，这列并没有默认值设定
    # title = models.CharField(max_length=32, default = "houhouhou")
    # nothing = models.IntegerField(null=True, blank=True)

# 效果：创建一个名为app01_userinfo的表，自带自增主键id列
# 还包含name varchar(32), password varchar(64), age int
    
# 测试用表
class onlyTitle(models.Model):
    title = models.CharField(max_length=16)