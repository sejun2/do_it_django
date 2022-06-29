from django.shortcuts import render
from .models import Post


# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-pk')  # -를 붙이면 역순표시

    return render(
        request,
        'blog/index.html',
        {
            'posts': posts,
        },
    )


def single_post_page(request, pk):
    try:
        post = Post.objects.get(pk=pk)

        return render(
            request,
            'blog/single_post_page.html',
            {
                'post': post,
            }
        )

    except BaseException as e:
        return render(
            request,
            'blog/not_found.html'
        )
