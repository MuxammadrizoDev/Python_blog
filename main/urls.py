from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('blog_detail/<int:id>/', views.blog_detail, name='blog_detail'),
    path('blog_list/', views.blog_list, name='blog_list'),
    path('contacts/', views.contacts, name='contacts'),
    path('blog-filter/<int:category_id>/', views.blog_filter, name='blog_filter'),
]