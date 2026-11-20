from django import forms
from .models import Patient

class PatientForm(forms.Form):
    name = forms.CharField(
        max_length=150,
        label="Patient Name"
    )
    age = forms.IntegerField(
        min_value=1,
        max_value=120
    )
    phone = forms.CharField(
        max_length=15
    )
    gender = forms.CharField(
        max_length=10
    )
    email = forms.EmailField()


class PatientModelForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            "name",
            "age",
            "phone",
            "gender",
            "email",
        ]

    def clean_phone(self):
        phone = self.cleaned_data.get("phone", "")

        if not phone.isdigit() or len(phone) != 10:
            raise forms.ValidationError(
                "Phone number must contain exactly 10 digits."
            )

        return phone
