from django.db import models
from . import managers


class TimeStampModel(models.Model):
    """ Time Stamped Model"""

    created = models.DateTimeField(auto_now_add=True)  # model 생성 날짜
    updated = models.DateTimeField(auto_now=True)  # save 할 때마다 새로운 시간 생성
    objects = managers.CustomModelManager()

    class Meta:
        abstract = True  # db 등록을 하지 않고 기능만을 위한 경우
