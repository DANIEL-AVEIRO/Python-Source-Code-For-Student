from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from core import views

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("", views.index, name="home"),
        # ========== Post URLs ==========
        path("post/list/", views.post_list, name="post_list"),
        path("post/create/", views.post_create, name="post_create"),
        path("post/update/<uuid:pk>/", views.post_update, name="post_update"),
        path("post/delete/<uuid:pk>/", views.post_delete, name="post_delete"),
        path("post/toggle/<uuid:pk>/", views.post_toggle, name="post_toggle"),
        path("post/details/<uuid:pk>/", views.post_details, name="post_details"),
        # ========== Category URLs ==========
        path("category/list/", views.category_list, name="category_list"),
        path("category/create/", views.category_create, name="category_create"),
        path(
            "category/update/<uuid:pk>/", views.category_update, name="category_update"
        ),
        path(
            "category/delete/<uuid:pk>/", views.category_delete, name="category_delete"
        ),
        # ========== Comment URLs ==========
        path(
            "comment/create/<uuid:post_pk>/",
            views.comment_create,
            name="comment_create",
        ),
        path("comment/delete/<uuid:pk>/", views.comment_delete, name="comment_delete"),
        # ========= Authentication URLs ==========
        path("login/", views.login_view, name="login"),
        path("logout/", views.logout_view, name="logout"),
        path("register/", views.register, name="register"),
        path("profile/", views.profile, name="profile"),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
