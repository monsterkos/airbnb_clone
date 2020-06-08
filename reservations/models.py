from django.db import models
from core import models as core_models

# Create your models here.


class Reservation(core_models.TimeStampModel):

    """ Reservatkon Model Definition """

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCLED = "canceled"

    STATUS_CHOICE = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCLED, "Canceled"),
    )

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICE, default=STATUS_PENDING
    )

    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room} - {self.check_in}"