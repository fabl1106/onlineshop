from django import forms

from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        # 너무 많아서 제외하는 것만 넣는다.
        exclude = ['created','updated','paid']

