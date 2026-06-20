from django.db import models
import uuid
from django.contrib.auth.models import User


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CategoryModel(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        db_table = "categories"


class PostModel(BaseModel):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="post_images")
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    category = models.ForeignKey(
        CategoryModel, on_delete=models.CASCADE, related_name="posts"
    )
    viewers = models.ManyToManyField(User, related_name="viewed_posts")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"
        db_table = "posts"


class CommentModel(BaseModel):
    post = models.ForeignKey(
        PostModel, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"

    class Meta:
        verbose_name_plural = "Comments"
        db_table = "comments"


class UserProfileModel(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    profile = models.ImageField(upload_to="profile_images", blank=True, null=True)

    class Meta:
        verbose_name_plural = "User Profiles"
        db_table = "user_profiles"
