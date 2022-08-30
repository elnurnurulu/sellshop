from django import forms
from blog.models import BlogComment


class BlogCommentForm(forms.ModelForm):

    class Meta:
        model = BlogComment
        fields = (
            'comment',
        )
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Name here'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email here'
            }),
            'comment': forms.Textarea(attrs={
                'cols': 40,
                'rows': 5,
                'placeholder': 'Comment here'
            })
        }

