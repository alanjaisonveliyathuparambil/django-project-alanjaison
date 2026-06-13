from django import forms
from django.contrib.auth.models import User
from .models import PickupRequest, ScrapMaterial


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter password'
        })
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class PickupRequestForm(forms.ModelForm):

    scrap_material = forms.ModelChoiceField(
        queryset=ScrapMaterial.objects.none(),
        empty_label="Select Scrap Material",
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    quantity = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': '1',
            'step': '1',
            'placeholder': 'Enter quantity in kg'
        })
    )

    class Meta:
        model = PickupRequest
        fields = [
            'scrap_material',
            'quantity',
            'pickup_address',
            'preferred_date',
            'notes'
        ]

        widgets = {
            'pickup_address': forms.Textarea(attrs={
                'class': 'form-control fixed-textarea',
                'rows': 4,
                'placeholder': 'Enter pickup address'
            }),

            'preferred_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'notes': forms.Textarea(attrs={
                'class': 'form-control fixed-textarea',
                'rows': 3,
                'placeholder': 'Any additional information'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(PickupRequestForm, self).__init__(*args, **kwargs)

        self.fields['scrap_material'].queryset = ScrapMaterial.objects.filter(
            is_active=True
        )


class ScrapMaterialForm(forms.ModelForm):
    class Meta:
        model = ScrapMaterial
        fields = ['name', 'category', 'price_per_kg', 'is_active']