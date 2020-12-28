from django.db import models

# Create your models here.
class Vip(models.Model):
    Vphone=models.PositiveIntegerField('电话号码',primary_key=True)
    Vusername=models.CharField('用户名',max_length=40)
    Vpassword=models.CharField('密码',max_length=15)
    Vrealname=models.CharField('姓名',max_length=40)
    Sex_choices=(('Man','男'),('Woman','女'))
    Vsex=models.CharField('性别',max_length=10,choices=Sex_choices)
    Vemail=models.EmailField('邮箱')#附加合法性验证
    Vaddress=models.CharField('地址',max_length=60)
    class Meta:
        verbose_name='会员'
        verbose_name_plural=verbose_name
class Bookmanager(models.Model):
    Mid=models.AutoField('工号',primary_key=True) #工号自动增长
    Mpassword=models.CharField('密码',max_length=15)
    Mrealname=models.CharField('姓名',max_length=40)
    class Meta:
        verbose_name='管理员'
        verbose_name_plural=verbose_name
        ordering=['Mid']
class Book(models.Model):
    Bisbn=models.PositiveIntegerField('ISBN',primary_key=True)
    Bname=models.CharField('书名',max_length=40)
    Bnumber=models.PositiveIntegerField('数量',default=0)
    Bauthor=models.CharField('作者',max_length=40)
    Bprice=models.DecimalField('价格', max_digits=7, decimal_places=2)
    Bcategory=models.CharField('类别',max_length=10)#没有考虑多种类别的情况
    Bpublisher=models.CharField('出版社',max_length=30)
    Bpublisherdate=models.DateField('出版日期',null=True)#可空
    Bintroduction=models.TextField('简介')
class Bookorder(models.Model):
    Oid=models.PositiveIntegerField('订单号')#不会自己生成
    Obook=models.ForeignKey('Book',related_name='Orderbook',on_delete=models.DO_NOTHING)
    Ovip=models.ForeignKey('Vip',related_name='Ordervip',on_delete=models.DO_NOTHING)
    Onumber=models.PositiveIntegerField('销售数量')
    Oprice=models.DecimalField('单价',max_digits=7, decimal_places=2)
    Odate=models.DateTimeField('购买时间',auto_now_add=True)
    class Meta:
        unique_together=("Oid","Obook")#双主键
class Sellrecord(models.Model):
    Sid=models.ForeignKey('Bookorder',related_name='Orderid',on_delete=models.DO_NOTHING)
    Sbook=models.ForeignKey('Book',related_name='Sellbook',on_delete=models.DO_NOTHING)
    Svip=models.ForeignKey('Vip',related_name='Sellvip',on_delete=models.DO_NOTHING)
    Snumber=models.PositiveIntegerField('销售数量')
    Sprice=models.DecimalField('单价',max_digits=7, decimal_places=2)
    Sdate=models.DateTimeField('购买时间',auto_now_add=True)
    class Meta:
        unique_together=("Sid","Sbook")#双主键
class Shoppingcar(models.Model):
    Cid=models.PositiveIntegerField('编号')#不会自己生成
    Cbook=models.ForeignKey('Book',related_name='Shoppingbook',on_delete=models.DO_NOTHING)
    Cvip=models.ForeignKey('Vip',related_name='Shoppingvip',on_delete=models.DO_NOTHING)
    Cnumber=models.PositiveIntegerField('数量')
    Cprice=models.DecimalField('单价',max_digits=7, decimal_places=2)
    class Meta:
        unique_together=("Cid","Cbook")
class Comment(models.Model):
    Coid=models.AutoField('留言编号',primary_key=True)
    Cobook=models.ForeignKey('Book',related_name='Commentbook',on_delete=models.DO_NOTHING)
    Covip=models.ForeignKey('Vip',related_name='Commentvip',on_delete=models.DO_NOTHING)
    Cocontent=models.TextField('留言内容')
    Cograde=models.PositiveIntegerField('评分')
class Commentlist(models.Model):#回复表
    comment=models.ForeignKey('Comment',related_name='comment',on_delete=models.DO_NOTHING)
    manager=models.ForeignKey('Bookmanager',related_name='manager',on_delete=models.DO_NOTHING)
    Recontent=models.TextField('留言回复')
