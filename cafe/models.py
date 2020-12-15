from django.db import models
import datetime

from django.db.models.deletion import CASCADE


class snacks(models.Model):
    """
    This model defines the fields in the "cafe_snacks" table.
    """
    name = models.CharField(max_length=100)
    price = models.FloatField()
    is_active = models.BooleanField()


class cart(models.Model):
    """
    This model defines the fields in the "cafe_cart" table.
    """
    emp_id = models.IntegerField(null=True)
    cart_id = models.IntegerField(null=True)
    snack = models.ForeignKey(to=snacks, on_delete=CASCADE, null=True)
    qty = models.IntegerField(null=True)
    date_time = models.DateField(default=datetime.date.today, null=True)
    ind_total = models.IntegerField(null=True)
    total = models.FloatField(null=True)
    payment_status = models.CharField(max_length=50)
    txn_id = models.CharField(max_length=200, null=True)
    emp_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return "Employee id: " + str(self.emp_id) + " and total: " + str(self.total)