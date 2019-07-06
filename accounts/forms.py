from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm
)


class LoginForm(AuthenticationForm):
    """ログインフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            # placeholderにフィールドのラベルを入れる
            field.widget.attrs['placeholder'] = field.label
            field.widget.attrs['required'] = 'required'


class SignUpForm(UserCreationForm):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
