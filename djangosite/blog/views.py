from .forms import EmailPostForm, PostForm
from .models import Post, Tag
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.text import slugify


# Create your views here.

class PostListView(ListView):
    queryset = Post.objects.filter(status=Post.PostStatus.PUBLISHED)
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    tags = post.tags.all()
    return render(request, 'blog/post/detail.html', {'post': post,
                                                     'tags': tags})


def post_shar(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post,
                                                    'form': form})


def blog_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/blog_list.html', {'tags': tags})


def posts_by_blog(request, tag_name):
    posts = Post.objects.filter(tags__tag_name=tag_name, status=Post.PostStatus.PUBLISHED)
    context = {'posts': posts,
               'tag_name': tag_name}
    return render(request, 'blog/posts_by_blog.html', context)


def home_list(request):
    posts = Post.objects.filter(status=Post.PostStatus.PUBLISHED)[:5]
    return render(request, 'blog/home.html', {'posts': posts})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish = timezone.now()
            post.slug = slugify(post.title)
            post.save()
            form.save_m2m()
            return redirect(post.get_absolute_url())
    else:
        form = PostForm()
    return render(request, 'blog/post/create_post.html', {'form': form})


@login_required
def edit_post(request, year, month, day, post):
    # Retrieve the post object based on the provided year, month, day, and post slug
    post = get_object_or_404(Post, slug=post, publish__year=year, publish__month=month, publish__day=day)

    if request.method == 'POST':
        # Create a form instance with the post data
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            # Save the updated post
            form.save()
            return redirect(post.get_absolute_url())
    else:
        # Create a form instance with the post data
        form = PostForm(instance=post)

    # Render the edit post template with the form
    return render(request, 'blog/post/edit_post.html', {'form': form, 'post': post})
