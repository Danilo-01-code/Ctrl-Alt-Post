from django.urls import path
from .views import BlogListView, BlogDetailView, BLogCreateView, BlogUpadateView, BlogDeleteView


urlpatterns = [
    path('post/new/',BLogCreateView.as_view(), name = 'post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(),
    name='post_detail'), 
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/edit/',BlogUpadateView.as_view(), name = 'post_edit'),
    path('post/<int:pk>/delete/',BlogDeleteView.as_view(), name = 'post_delete')
]