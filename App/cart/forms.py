from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(25, 100 + 1, 25)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        label='Вес',
    )
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
