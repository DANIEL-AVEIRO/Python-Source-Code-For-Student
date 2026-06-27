from core.models import PostModel, CategoryModel, CommentModel, UserProfileModel
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q


# ====================
# Home
# ====================
def index(request):
    search = request.GET.get("search")
    posts = PostModel.objects.filter(is_active=True).order_by("-created_at")
    if search:
        posts = posts.filter(
            Q(title__icontains=search)
            | Q(content__icontains=search)
            | Q(category__name__icontains=search)
            | Q(author__username__icontains=search)
        )
    context = {"posts": posts, "search": search}
    return render(request, "index.html", context)


# ====================
# Post List
# ====================
@login_required(login_url="login")
def post_list(request):
    search = request.GET.get("search")
    posts = PostModel.objects.filter(is_active=True).order_by("-created_at")
    if search:
        posts = posts.filter(title__icontains=search)
    context = {"posts": posts, "search": search}
    return render(request, "post_list.html", context)


# ====================
# Post Create
# ====================
@login_required(login_url="login")
def post_create(request):
    categories = CategoryModel.objects.all()
    if request.method == "GET":
        context = {"categories": categories}
        return render(request, "post_create.html", context)
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        category = request.POST.get("category")
        image = request.FILES.get("image")
        author = request.user.id
        post = PostModel.objects.create(
            title=title,
            content=content,
            category_id=category,
            image=image,
            author_id=author,
        )
        post.save()
        messages.success(request, "Post created successfully")
        return redirect("post_list")


# ====================
# Post Update
# ====================
@login_required(login_url="login")
def post_update(request, pk):
    post = PostModel.objects.get(id=pk)
    categories = CategoryModel.objects.all()
    if request.method == "GET":
        context = {"post": post, "categories": categories}
        return render(request, "post_update.html", context)
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        category = request.POST.get("category")
        image = request.FILES.get("image")
        post.title = title
        post.content = content
        post.category_id = category
        if image:
            if post.image:
                post.image.delete()
            post.image = image
        post.save()
        messages.success(request, "Post updated successfully")
        return redirect("post_list")


# ====================
# Post Delete
# ====================
@login_required(login_url="login")
def post_delete(request, pk):
    post = PostModel.objects.get(id=pk)
    if post.image:
        post.image.delete()
    post.viewers.clear()
    post.delete()
    messages.success(request, "Post deleted successfully")
    return redirect("post_list")


# ====================
# Post Details
# ====================
@login_required(login_url="login")
def post_details(request, pk):
    post = PostModel.objects.get(id=pk)
    comments = CommentModel.objects.filter(post_id=pk)
    if request.user.is_authenticated and request.user not in post.viewers.all():
        post.viewers.add(request.user)
    context = {"post": post, "comments": comments}
    return render(request, "post_details.html", context)


# ====================
# Post Toggle
# ====================
@login_required(login_url="login")
def post_toggle(request, pk):
    post = PostModel.objects.get(id=pk)
    if post.is_active:
        post.is_active = False
        status = "deactivated"
    else:
        post.is_active = True
        status = "activated"
    post.save()
    messages.success(request, f"Post {status} successfully")
    return redirect("post_list")


# ====================
# Category List
# ====================
@login_required(login_url="login")
def category_list(request):
    categories = CategoryModel.objects.all().order_by("-created_at")
    context = {"categories": categories}
    return render(request, "category_list.html", context)


# ====================
# Category Create
# ====================
@login_required(login_url="login")
def category_create(request):
    if request.method == "GET":
        return render(request, "category_create.html")
    if request.method == "POST":
        name = request.POST.get("name")
        category = CategoryModel.objects.create(name=name)
        category.save()
        messages.success(request, "Category created successfully")
        return redirect("category_list")


# ====================
# Category Update
# ====================
@login_required(login_url="login")
def category_update(request, pk):
    category = CategoryModel.objects.get(id=pk)
    if request.method == "GET":
        context = {"category": category}
        return render(request, "category_update.html", context)
    if request.method == "POST":
        name = request.POST.get("name")
        category.name = name
        category.save()
        messages.success(request, "Category updated successfully")
        return redirect("category_list")


# ====================
# Category Delete
# ====================
@login_required(login_url="login")
def category_delete(request, pk):
    category = CategoryModel.objects.get(id=pk)
    category.delete()
    messages.success(request, "Category deleted successfully")
    return redirect("category_list")


# ====================
# Login
# ====================
def login_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("home")
        return render(request, "login.html")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")


# ====================
# Register
# ====================
def register(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("home")
        return render(request, "register.html")
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("register")
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect("register")
        user = User.objects.create_user(
            username=username, email=email, password=password
        )
        user.save()
        user_profile = UserProfileModel.objects.create(user=user)
        user_profile.save()
        messages.success(request, "Registered successfully. Please log in.")
        return redirect("login")


# ====================
# Logout
# ====================
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("home")


# ====================
# Comment Create
# ====================
@login_required(login_url="login")
def comment_create(request, post_pk):
    if request.method == "POST":
        content = request.POST.get("content")
        author = request.user.id
        comment = CommentModel.objects.create(
            content=content, author_id=author, post_id=post_pk
        )
        comment.save()
        messages.success(request, "Comment added successfully")
        return redirect("post_details", pk=post_pk)


# ====================
# Comment Delete
# ====================
@login_required(login_url="login")
def comment_delete(request, pk):
    comment = CommentModel.objects.get(id=pk)
    comment.delete()
    messages.success(request, "Comment deleted successfully")
    return redirect("post_details", pk=comment.post.id)


# ====================
# Profile
# ====================
@login_required(login_url="login")
def profile(request):
    user_profile = UserProfileModel.objects.get(user_id=request.user.id)
    if request.method == "GET":
        context = {}
        return render(request, "profile.html", context)
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        bio = request.POST.get("bio")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        profile = request.FILES.get("profile")

        user = User.objects.get(id=request.user.id)
        user.username = username
        user.email = email
        user.save()

        user_profile = UserProfileModel.objects.get(user=user)
        user_profile.bio = bio
        user_profile.phone = phone
        user_profile.address = address
        if profile:
            if user_profile.profile:
                user_profile.profile.delete()
            user_profile.profile = profile
        user_profile.save()
        messages.success(request, "Profile updated successfully")
        return redirect("profile")


# ====================
# Page Not Found
# ====================
def page_not_found(request):
    return render(request, "page_not_found.html")
