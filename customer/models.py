from django.db import models
from owner.models import Mobile

# Create your models here.


class Cart(models.Model):
    product=models.ForeignKey(Mobile,on_delete=models.CASCADE)
    options=(
        ("in_cart","in_cart"),
        ("order_place","order_place"),
        ("order_cancelled","order_cancelled")
    )
    status=models.CharField(max_length=40,default="in_cart",choices=options)
    user=models.CharField(max_length=30)


class Orders(models.Model):
    product=models.ForeignKey(Mobile,on_delete=models.CASCADE)
    address=models.CharField(max_length=250)
    qty=models.PositiveIntegerField(default=1)
    options=(
        ("order_placed","order_placed"),
        ("dispatched","dispatched"),
        ("intransmit","intransmit"),
        ("deliverd","deliverd"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=120,default="order_placed",choices=options)
    user=models.CharField(max_length=120)
