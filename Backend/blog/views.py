from accounts.models import ExtraUserInfo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import Http404
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render

from .forms import CategoryForm, CommentForm, PostForm
from .models import Category, Comments, Post

# Create your views here.

# Category CURD Operation:
# Create operation:
@login_required
def create_category(request):
    context = {}
    user_extra = ExtraUserInfo.objects.filter(user_info=request.user)
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    context['form'] = form
    context = {
        'user_extra':user_extra,
        'form':form
    }
    return render(request, 'blog/create_category.html', context)


# Read operation:
def list_category(request):
    context = {}
    user_extra = ExtraUserInfo.objects.filter(user_info=request.user)
    dataset = Category.objects.all()
    category = Category.objects.all()

    context = {
        'user_extra':user_extra,
        'dataset':dataset,
        'category':category
    }
    return render(request, 'blog/list_category.html', context)

@login_required
# Update  operation:
def update_category(request, id):
    context = {}
    obj = get_object_or_404(Category, id=id)
    user_extra = ExtraUserInfo.objects.filter(user_info=request.user)
    form = CategoryForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/'+id)
    context['form'] = form
    return render(request, 'blog/update_category.html', context)

@login_required
# Delete operation:
def delete_category(request, id):
    context = {}
    user_extra = ExtraUserInfo.objects.filter(user_info=request.user)
    obj = get_object_or_404(Category, id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, "blog/delete_category.html", context)


# Post view CURD Operation:
# Read operation:
def list_post(request):
    object_list = {}
    category = {}

    category = Category.objects.all()
    object_list = Post.objects.all()
    
    if request.user.is_authenticated:
        user_extra = ExtraUserInfo.objects.filter(user_info=request.user)
    else:
        user_extra = 'Guest user'

    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)
    context = {
        'page': page,
        'post_list': post_list,
        'object_list': object_list,
        'category': category,
        'user_extra': user_extra
    }
    return render(request, 'blog/home.html', context)

@login_required
# Create operation:
def create_post(request):
    context = {}
    user_extra = ExtraUserInfo.objects.filter(user_info=request.user)
    if request.user.is_authenticated:
        form = PostForm(request.POST or None )
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return HttpResponseRedirect('/')

        context['form'] = form
        context = {
            'form':form,
            'user_extra':user_extra
        }
    return render(request, 'blog/create_post.html', context)

@login_required
# Update  operation:
def update_post(request, id):
    context = {}

    obj = get_object_or_404(Post, id=id)
    category = Category.objects.all()
    user_extra = ExtraUserInfo.objects.filter(user_info=request.user)
    form = PostForm(request.POST or None, instance=obj)
    
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        return HttpResponseRedirect('/'+id)
    context = {
        'user_extra': user_extra,
        'form': form,
        'category':category,
        'obj':obj
    }
    return render(request, 'blog/update_post.html', context)

@login_required
# Delete operation:
def delete_post(request, id):
    context = {}
    category = Category.objects.all()
    user_extra = ExtraUserInfo.objects.filter(user_info=request.user)
    obj = get_object_or_404(Post, id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")

    context = {
        'obj':obj,
        'user_extra':user_extra,
        'category':category
    }
    return render(request, "blog/delete_post.html", context)

@login_required
# Detail  operation:
def detail_post(request, id):
    post = {}
    user_extra = ExtraUserInfo.objects.filter(user_info=request.user)
    category = Category.objects.all()
    post = get_object_or_404(Post, id=id)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'category': category,
        'user_extra': user_extra

    }
    return render(request, 'blog/detail_post.html', context)

@login_required
# Comment CURD Operations:
# Update Comments:
def update_comments(request, id):
    context = {}
    obj = get_object_or_404(Comments, id=id)
    category = Category.objects.all()
    user_extra = ExtraUserInfo.objects.filter(user_info=request.user)
    form = CommentForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/'+id)
    context= {
        'category':category,
        'form': form,
        'user_extra': user_extra
    }
    return render(request, 'comments/update_comments.html', context)

@login_required
# Delete operation:
def delete_comments(request, id):
    context = {}
    user_extra = ExtraUserInfo.objects.filter(user_info=request.user)
    category = Category.objects.all()
    obj = get_object_or_404(Comments, id=id)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")

    context ={
        'obj': obj,
        'user_extra':user_extra,
        'category': category

    }
    return render(request, "comments/delete_comments.html", context)
