from django import forms
from .models import Post, Comment, Category

choices = Category.objects.all().values_list('name','name')
cat_list = []

for cat in choices:
    cat_list.append(cat)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'imageURL', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'O título da sua postagem', 'label': 'alo'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.CheckboxSelectMultiple(choices=cat_list),
            'imageURL': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Link de uma imagem associada à postagem'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'O conteúdo da postagem'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'imageURL', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'O título da sua postagem', 'label': 'alo'}),
            'category': forms.CheckboxSelectMultiple(choices=cat_list),
            'imageURL': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Link de uma imagem associada à postagem'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'O conteúdo da postagem'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'body')

        widgets = {
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'O conteúdo do comentário'}),
        }