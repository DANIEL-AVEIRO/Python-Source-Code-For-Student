from django.contrib import admin
from core import models

admin.site.register(models.CategoryModel)
admin.site.register(models.PostModel)
admin.site.register(models.CommentModel)
admin.site.register(models.UserProfileModel)
