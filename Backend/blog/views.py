from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render

from .forms import PostForm
from .models import Category, Post


# Create your views here.
# Read operation:
def list_post(request):
    object_list = {}
    category = {}

    category = Category.objects.all()
    object_list = Post.objects.all()

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
    }
    return render(request, 'blog/list_post.html', context)

# Post view
# Create operation:
def create_post(request):
    context = {}
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect('/')
    context['form'] = form
    return render(request, 'blog/create_post.html', context)
