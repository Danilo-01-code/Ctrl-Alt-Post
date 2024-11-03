from django.urls import path
from .views import *


urlpatterns = [
    path('post/new/',BlogCreateView.as_view(), name = 'post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(),
    name='post_detail'), 
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/edit/',BlogUpadateView.as_view(), name = 'post_edit'),
    path('post/<int:pk>/delete/',BlogDeleteView.as_view(), name = 'post_delete'),
    path('signup/', signupView, name = 'signup'),
    path('post/<int:pk>/comment/',CommentCreateView.as_view(),name = 'new_comment'),
]