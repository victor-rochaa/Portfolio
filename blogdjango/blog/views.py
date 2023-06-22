from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, Category
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy

def handler404(request, exception):
    return render(request, '404.html')

class Home(ListView):
    model = Post
    template_name = 'home.html'

class Posts(ListView):
    model = Post
    template_name = 'posts.html'
    ordering = ['-datetime'] # coloca os posts mais recentes primeiro

class PostDetail(DetailView):
    model = Post
    template_name = 'post_details.html'

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class UpdatePost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ('title', 'imageURL', 'body')

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('posts')

class AddComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    #fields = '__all__'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})

class Categories(ListView):
    model = Category
    template_name = 'categories.html'
    fields = '__all__'

def CategoryDetail(request, cat_id):
    cat = get_object_or_404(Category, pk=cat_id)
    return render(request, 'category_details.html', {'cat':cat})