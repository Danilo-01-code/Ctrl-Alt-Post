from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/password_change/', views.PasswordChangeView.as_view(template_name='password_change_form.html'), name='password_change'),
    path('accounts/password_change/done/',views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),name='password_change_done'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('',include('blog.urls')),
   
]

