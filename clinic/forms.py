from django import forms
from .models import Appointment,CallRequest
from pages.models import OmsRequest


def validate_phone(phone):
    allowed = '0123456789+ ()-'
    
    if not all(ch in allowed for ch in phone):
        raise forms.ValidationError('Телефон может содержать только цифры, +, пробелы, скобки и дефисы.')
    
    digits = sum(1 for ch in phone if ch.isdigit())
    if digits < 10:
        raise forms.ValidationError('Введите не менее 10 цифр.')
    
    return phone


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['full_name','phone','direction','doctor']
    def clean_phone(self):
        return validate_phone(self.cleaned_data['phone'])


class CallRequestForm(forms.ModelForm):
    class Meta:
        model = CallRequest
        fields = ['full_name','phone']
    def clean_phone(self):
        return validate_phone(self.cleaned_data['phone'])
        
class OmsRequestForm(forms.ModelForm):
    agree = forms.BooleanField(
        required=True,
        error_messages={'required': 'Нужно согласие на обработку данных.'})
    class Meta:
        model = OmsRequest
        fields = ['full_name', 'date_birthday', 'email', 'phone_number',
          'profile', 'service', 'region', 'representative',
          'reason', 'source', 'document']
        
    def clean_phone_number(self):
        return validate_phone(self.cleaned_data['phone_number'])