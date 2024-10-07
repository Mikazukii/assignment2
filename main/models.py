from django.db import models
import uuid
from django.contrib.auth.models import User


# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     prix = models.IntegerField()
#     description = models.TextField()


class ProductEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    feedback = models.TextField()
    note = models.IntegerField()

    @property
    def is_product_good(self):
        return self.note > 5
