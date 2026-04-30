from django import forms
from django.contrib.auth.models import User
from .models import Post, Profile, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'body', 'status', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'НАЗВА ЗАПИСУ...'}),
            'category': forms.Select(),
            'body': forms.Textarea(attrs={'placeholder': 'ТЕКСТ...', 'rows': 5}),
            'status': forms.Select(),
            'image': forms.FileInput(),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = True
        self.fields['image'].help_text = ""
        self.fields['title'].label = "TITLE"
        self.fields['category'].label = "CATEGORY"
        self.fields['body'].label = "DESCRIPTION"
        self.fields['status'].label = "STATUS"
        self.fields['image'].label = "IMAGE (REQUIRED)"

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'placeholder': 'НАПИШІТЬ КОМЕНТАР...',
                'class': 'border-1 w-100 p-3',
                'rows': 3,
                'style': 'border: 1px solid #000; outline: none;'
            }),
        }