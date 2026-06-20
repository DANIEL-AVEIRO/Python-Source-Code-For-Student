from django.db import models
from models.base_models import BaseModel
from django.contrib.auth.models import User
from core.models import CategoryModel


class PostModel(BaseModel):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="post_images")
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    category = models.ForeignKey(
        CategoryModel, on_delete=models.CASCADE, related_name="posts"
    )
    viewers = models.ManyToManyField(User, related_name="viewed_posts")
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"
        app_label = "core"
        db_table = "posts"
