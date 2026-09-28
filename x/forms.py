from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import X


class XForm(forms.ModelForm):
    class Meta:
        model = X
        fields = ["text", "photo"]

        widgets = {
            "text": forms.Textarea(
                attrs={
                    "rows": 4,
                    "maxlength": 300,
                    "placeholder": "What's happening?",
                }
            ),
        }

    def clean_text(self):
        text = self.cleaned_data["text"].strip()

        if not text:
            raise forms.ValidationError("Post text cannot be empty.")

        return text


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        max_length=254,
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                "An account with this email already exists."
            )

        return email