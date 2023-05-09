from .models import Comment
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.template import Context


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


# class RegisterForm(UserCreationForm):
#     email = forms.EmailField(max_length=254)

#     class Meta:
#         model = User
#         fields = ('username',  'email', 'password1', 'password2', )


# for profile update
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']


def save(self):
    user = super().save()
    x = self.cleaned_data.get('x')
    y = self.cleaned_data.get('y')
    w = self.cleaned_data.get('width')
    h = self.cleaned_data.get('height')

    image = Image.open(self.image)
    cropped_image = image.crop((x, y, w + x, h + y))
    resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)

    fh = storage.open(self.image.name, "w")
    picture_format = 'png'
    resized_image.save(fh, picture_format)
    fh.close()
    resized_image.save(self.image.path)
    return user
