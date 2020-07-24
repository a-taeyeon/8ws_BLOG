from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import BlogPost
# Create your views here.

def home(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs': blogs, 'posts': posts})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'details':details})

def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    blog.delete()
    return redirect('home')

def create(request):
    if request.method =='POST': #입력된 내용을 처리해주는 기능
        form = BlogPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return redirect('home')
    else:   #빈페이지를 띄워주는 기능
        form = BlogPost()
        return render(request,'create.html',{'form':form})

def update(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)

    if request.method == 'POST':
        form = BlogPost(request.POST, request.FILES, instance = blog)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = BlogPost(instance = blog)
        return render(request, 'create.html', {'form':form})