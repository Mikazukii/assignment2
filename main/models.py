from django.db import models
import uuid


# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     prix = models.IntegerField()
#     description = models.TextField()


class ProductEntry(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )  # add this line
    product_name = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    feedback = models.TextField()
    note = models.IntegerField()

    @property
    def is_product_good(self):
        return self.note > 5
