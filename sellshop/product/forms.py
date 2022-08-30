from django import forms
from product.models import ProductReview


class ProductReviewsForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = (
            'review',
        )
        widgets = {
            'review': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Your review'
            })
        }
