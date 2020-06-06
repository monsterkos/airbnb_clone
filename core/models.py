from django.db import models

# Create your models here.


class TimeStampModel(models.Model):
    """ Time Stamped Model"""

    created = models.DateTimeField(auto_now_add=True)  # model 생성 날짜
    updated = models.DateTimeField(auto_now_add=True)  # save 할 때마다 새로운 시간 생성

    class Meta:
        abstract = True  # db 등록을 하지 않고 기능만을 위한 경우
