from django.db import models
from models.base_models import BaseModel


class CategoryModel(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        app_label = "core"
        db_table = "categories"
