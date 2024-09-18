from django import forms
from .models import Student, Course, Batch, Trainer, Topic

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'country_code', 'mobile_number', 'course', 'batch']

    first_name = forms.CharField(max_length=40, required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=40, required=True, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(max_length=60, required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email ID'}))
    country_code = forms.ChoiceField(choices=[('+91', 'India (+91)'), ('+1', 'USA (+1)'), ('+44', 'UK (+44)')], required=True, initial='+91')
    mobile_number = forms.CharField(max_length=10, required=True, widget=forms.TextInput(attrs={'placeholder': 'Mobile Number'}))

    # Remove the filters related to is_active and is_open
    course = forms.ModelChoiceField(queryset=Course.objects.all(), required=True)
    batch = forms.ModelChoiceField(queryset=Batch.objects.all(), required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Only gmail.com email addresses are allowed. Please enter a valid gmail address.")
        return email

    def clean_mobile_number(self):
        mobile_number = self.cleaned_data.get('mobile_number')
        if not mobile_number.isdigit():
            raise forms.ValidationError("Mobile number must contain only digits.")
        if len(mobile_number) != 10:
            raise forms.ValidationError("Mobile number must be exactly 10 digits.")
        return mobile_number

    def clean(self):
        cleaned_data = super().clean()
        for field in self.Meta.fields:
            value = cleaned_data.get(field)
            if not value:
                raise forms.ValidationError(f"Please fill out the {field.replace('_', ' ')} field.")
        return cleaned_data

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'duration', 'mobile_number_1', 'mobile_number_2', 'trainer', 'topics', 'fee']

    trainer = forms.ModelChoiceField(
        queryset=Trainer.objects.all(),  # Remove is_active filter
        required=True,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    topics = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(),  # Remove is_active filter
        required=True,
        widget=forms.CheckboxSelectMultiple
    )
    duration = forms.IntegerField(
        min_value=30,
        max_value=200,
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duration in days'})
    )
    mobile_number_1 = forms.CharField(
        max_length=10,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number 1'})
    )
    mobile_number_2 = forms.CharField(
        max_length=10,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number 2'})
    )
    fee = forms.IntegerField(
        min_value=5000,
        max_value=80000,
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Fee'})
    )

    def clean_duration(self):
        duration = self.cleaned_data.get('duration')
        if duration < 30 or duration > 200:
            raise forms.ValidationError("Duration must be between 30 and 200 days.")
        return duration

    def clean_fee(self):
        fee = self.cleaned_data.get('fee')
        if fee < 5000 or fee > 80000:
            raise forms.ValidationError("Fee must be between 5000 and 80000.")
        return fee
