from django.db import models

# Create your models here.
class TaobaoSearch(models.Model):
    '''对应一次在淘宝上的搜索
    '''
    title = models.CharField(max_length = 100) # 卡牌名称

    def __str__(self):
        return self.title

