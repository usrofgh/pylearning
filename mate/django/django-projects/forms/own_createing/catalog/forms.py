from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

from catalog.models import Author, Book


class AuthorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Author
        fields = UserCreationForm.Meta.fields + ("email", "first_name", "last_name")

    # more custom approach
    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        if "putin" in last_name:
            raise ValidationError("Ammm. No.")

        return last_name


class AuthorUpdateForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Author
        fields = ("email",)




# class AuthorUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Author
#         fields = ("username", "first_name", "last_name", "email")
#
#     def clean_last_name(self):
#         last_name = self.cleaned_data["last_name"]
#         if "putin" in last_name:
#             raise ValidationError("Ammm. No.")

        # return last_name


class BookForm(forms.ModelForm):
    authors = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Book
        fields = "__all__"


class BookSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",  # delete title
        widget=forms.TextInput(attrs={"placeholder": "Search by title"})
    )
