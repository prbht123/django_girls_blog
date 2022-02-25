
from django.urls import path,include
from . import views

urlpatterns = [
 #   path('post/',views.index,name='index'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/get/',views.get_user,name='post_all_detail'),
    path('post/edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('post/view/<int:pk>', views.get_post_user, name='post_detail'),
  
]