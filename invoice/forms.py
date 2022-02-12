from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from .models import *
import json
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime


#Form Layout from Crispy Forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column



class DateInput(forms.DateInput):
    input_type = 'date'


class UserLoginForm(forms.ModelForm):
    username = forms.CharField(
                            widget=forms.TextInput(attrs={'id': 'floatingInput', 'class': 'form-control mb-3'}),
                            required=True)
    password = forms.CharField(
                            widget=forms.PasswordInput(attrs={'id': 'floatingPassword', 'class': 'form-control mb-3'}),
                            required=True)

    class Meta:
        model=User
        fields=['username','password']




class ClientForm(forms.ModelForm):

    clientCode = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'floatingInput', 'class': 'form-control mb-3'}),
        required=False, label='کد مشتری')

    clientName = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'floatingInput', 'class': 'form-control mb-3'}),
        required=True, label='نام مشتری')

    clientWork = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'floatingInput', 'class': 'form-control mg-3'}),
        required=False, label='زمینه فعالیت' )


    emailAddress = forms.CharField(
        widget=forms.EmailInput(attrs={'id': 'floatingInput', 'class': 'form-control mb-3'}),
        required=False, label='ایمیل')



    class Meta:
        model = Client
        fields = ['clientCode','clientName',  'clientWork', 'emailAddress' ]



class ProductForm(forms.ModelForm):


    title = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'floatingInput', 'class': 'form-control mb-3'}),
        required=True, label='نام محصول')

    quantity = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'floatingInput', 'class': 'form-control col-md-6'}),
        required=True, label='تعداد')

    description = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'floatingInput', 'class': 'form-control mb-3'}),
        required=False, label='توضیحات محصول')

    unit = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'floatingInput', 'class': 'form-control mb-3'}),
        required=True, label='واحد')

    class Meta:
        model = Product
        fields = ['title', 'quantity', 'description','unit']


class InvoiceForm(forms.ModelForm):

    title = forms.CharField(
                    label='شماره سفارش',
                    required=True,
                    widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'شماره سفارش'}))

    # create_Date = forms.CharField(
    #     required=True,
    #     label='تاریخ ثبت سفارش ',
    #     widget=forms.TextInput(attrs={'class': 'form-control mb-3 '}))

    request_code = forms.CharField(
                    label='شماره / کد درخواست کالا',
                    widget=forms.TextInput(attrs={'class': 'form-control mb-3 '}),required=True)

    # dueDate = forms.CharField(
    #                     required = True,
    #                     label='تاریخ تحویل سفارش ',
    #     widget=forms.TextInput(attrs={'class': 'form-control mb-3 '}))

    def __init__(self, *args, **kwargs):
        super(InvoiceForm, self).__init__(*args, **kwargs)
        self.fields['create_Date'] = JalaliDateField(label= ('تاریخ ثبت سفارش'),
                                                     widget=AdminJalaliDateWidget
                                                     )
        self.fields['dueDate'] = JalaliDateField(label=('تاریخ تحویل سفارش'),
                                                     widget=AdminJalaliDateWidget
                                                     )

    class Meta:
        model = Invoice
        fields = ['title', 'dueDate', 'create_Date', 'form_Number', 'request_code']


class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ['clientName', 'clientLogo', 'addressLine1', 'province', 'postalCode', 'phoneNumber', 'emailAddress', 'taxNumber']


class ClientSelectForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        self.initial_client = kwargs.pop('initial_client')
        self.CLIENT_LIST = Client.objects.all()
        self.CLIENT_CHOICES = [('-----', '--انتخاب مشتری--')]


        for client in self.CLIENT_LIST:
            d_t = (client.uniqueId, client.clientName)
            self.CLIENT_CHOICES.append(d_t)


        super(ClientSelectForm,self).__init__(*args,**kwargs)

        self.fields['client'] = forms.ChoiceField(
                                        label='انتخاب مشتری مربوطه',
                                        choices = self.CLIENT_CHOICES,
                                        widget=forms.Select(attrs={'class': 'form-control mb-3'}),)

    class Meta:
        model = Invoice
        fields = ['client']


    def clean_client(self):
        c_client = self.cleaned_data['client']
        if c_client == '-----':
            return self.initial_client
        else:
            return Client.objects.get(uniqueId=c_client)





















# <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
# <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
