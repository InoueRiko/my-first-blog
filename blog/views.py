from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_at__lte=timezone.now()).order_by('published_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

# Create your views here.def post_list(request):    return render(request, 'blog/post_list.html', {})from django.shortcuts import renderfrom .models import PosPost.objects.filter(published_date__lte=timezone.now()).order_by('published_date')