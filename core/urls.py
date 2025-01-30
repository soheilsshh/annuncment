from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home , name='home'),
    path('login/',views.sign_in, name = 'sign_in' ),
    path('sign_up/', views.sign_up , name = 'sign_up'),
    path('post/<int:post_id>/' , views.post_detail , name = 'post_detail'),
    path('post_ad/' , views.post_ad , name = 'post_ad'),
    path('user_post/' , views.user_post , name = 'user_post'),
    path('update_post/<int:post_id>/' , views.update_post , name = 'update_post'),
    path('delete_post/<int:post_id>/' , views.delete_post , name = 'delete_post'),
    path('search/', views.home , name = 'search')
]
