from django.db import models

# Create your models here.

class Card_EN(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return "Name: %s" % self.name

class Card_CN(models.Model):
    en = models.OneToOneField(Card_EN, primary_key=True)
    cn = models.CharField(max_length=100)
    def __str__(self):
        return "卡牌名称: %s/%s" % (self.cn, self.en)

