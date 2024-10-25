# views.py
from .models import Post
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView): 
    model = Post
    template_name = 'post_detail.html'

class BLogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title','author','body']

class BlogUpadateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

def signupView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})