from django.urls import path, include


from blog import views # 현재 폴더에 있는 views.py 을 사용할 수 있게 import

urlpatterns = [
    # path('/', views.index),
    path('/', views.PostList.as_view()),
    # path('/<int:pk>', views.single_post_page),
    path('/<int:pk>', views.PostDetail.as_view()),
]
