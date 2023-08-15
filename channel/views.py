from django.shortcuts import render, redirect
from .models import Channel
from .forms import PostForm


def index(request):
    context = {
        'posts': Channel.objects.all()
    }
    return render(request, 'channel/index.html', context)


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'channel/post_new.html', {'form': form})
