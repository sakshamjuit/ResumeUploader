from django import forms
from .models import Resume

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

CITY_CHOICES = (
    ('Bombay', 'Bombay'),
    ('Chennai', 'Chennai'),
    ('Delhi', 'Delhi')
)


class ResumeForms(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(choices=CITY_CHOICES, label='Preferred Job Location',
                                         widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Resume
        fields = '__all__'
        labels = {
            'name': 'Full Name',
            'dob': 'Date of Birth',
            'pincode': 'Pin code',
            'gender': 'Gender',
            'locality': 'Locality',
            'email': 'Email Address',
            'job_city': 'Job City',
            'profile_image': 'Profile Image',
            'my_file': 'Document'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pincode': forms.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),

        }
