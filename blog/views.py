# views.py
from .models import Post
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, CommentForm
from django.views import View


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'  # Adiciona o nome do contexto

    def get_queryset(self):
        # Retorna os posts em ordem decrescente
        return Post.objects.all().order_by('-date')



class BlogDetailView(DetailView): 
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('home')  # Redireciona para a página inicial ou outra URL após a criação

    def form_valid(self, form):
        form.instance.author = self.request.user  # Atribui o autor ao post
        return super().form_valid(form)
    

class BlogUpadateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','body']
  

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


class CommentCreateView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm()  
        return render(request, 'new_comment.html', {'form': form, 'post': post})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm(request.POST)  # Preenchendo o formulário com dados do POST
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post  # Associando o comentário ao post
            comment.author = request.user  # Associando o autor ao comentário
            comment.save()
            return redirect('post_detail', pk=post.pk)
        return render(request, 'new_comment.html', {'form': form, 'post': post})


def signupView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password']) 
            user.save()
            return redirect('login') 
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})