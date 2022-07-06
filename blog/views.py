from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


# Create your views here.

class PostList(ListView):
    model = Post
    # template_name = 'blog/index.html'
    ordering = '-pk'


class PostDetail(DetailView):
    model = Post

    ######## FBV ##########
# def index(request):
#     posts = Post.objects.all().order_by('-pk')  # -를 붙이면 역순표시
#
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts': posts,
#         },
#     )
#
#
# def single_post_page(request, pk):
#     try:
#         post = Post.objects.get(pk=pk)
#
#         return render(
#             request,
#             'blog/post_detail.html',
#             {
#                 'post': post,
#             }
#         )
#
#     except Exception as e:
#         return render(
#             request,
#             'blog/not_found.html'
#         )
