from django import forms

from .models import Orders


class OrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # меняем отображение описания формы
        self.fields['order_date'].label = 'Дата получения заказа'


    # добавляем вместо ручного ввода даты, календарь
    order_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Orders
        fields = (
            'first_name', 'last_name', 'phone', 'address', 'buying_type', 'order_date', 'comment'
        )
