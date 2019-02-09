from django import forms

category_choices = (
    ('food', '食費'),    # DB値 : 人に読みやすい表示
    ('fare', '交通費'),
    ('medical', '医療費'),
    ('tuition', '学費'),
    ('amusement', '娯楽費'),
    ('tax', '税金'),
    ('communication', '通信費'),
    ('clothes', '衣料品'),
    ('others', '雑費'),
)

class ExpenditureForm(forms.Form):
    used_date = forms.DateField(
        label='日付',
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control mr-2',
                'id' : 'date_choice',
                'style' : 'width:120px'
            }
        )
    )

    cost = forms.IntegerField(
        label='金額',
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control mr-2',
                'style' : 'width:80px'
            }
        )
    )

    money_use = forms.CharField(
        max_length=200,
        label='用途',
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control mr-5',
                'style' : 'width:370px'
            }
        )
    )

    category = forms.ChoiceField(
        choices=category_choices,
        label='カテゴリー',
        widget=forms.Select(
            attrs={
                'class' : 'form-control'
            }
        )
    )
