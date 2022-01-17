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

    clientName = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'floatingInput', 'class': 'form-control mb-3'}),
        required=True, label='نام مشتری')

    addressLine1 = forms.CharField(
    widget = forms.Textarea(attrs={'id': 'floatingInput', 'class': 'form-control mb-3'}),
             required = False, label = 'آدرس')

    province = forms.CharField(
    widget = forms.TextInput(attrs={'id': 'floatingInput', 'class': 'form-control mb-3'}),
             required = False, label = 'استان')

    postalCode = forms.CharField(
    widget = forms.NumberInput(attrs={'id': 'floatingInput', 'class': 'form-control mb-3'}),
             required = False, label = 'کد پستی')

    phoneNumber = forms.CharField(
        widget=forms.NumberInput(attrs={'id': 'floatingInput', 'class': 'form-control mb-3'}),
        required=True, label='شماره تماس')

    emailAddress = forms.CharField(
        widget=forms.EmailInput(attrs={'id': 'floatingInput', 'class': 'form-control mb-3'}),
        required=False, label='ایمیل')

    taxNumber = forms.CharField(
        widget=forms.NumberInput(attrs={'id': 'floatingInput', 'class': 'form-control mb-3'}),
        required=False, label='شماره مالیاتی')

    class Meta:
        model = Client
        fields = ['clientName', 'clientLogo', 'addressLine1', 'province', 'postalCode', 'phoneNumber', 'emailAddress', 'taxNumber']



class ProductForm(forms.ModelForm):


    title = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'floatingInput', 'class': 'form-control mb-3'}),
        required=True, label='نام محصول')

    quantity = forms.CharField(
        widget=forms.NumberInput(attrs={'id': 'floatingInput', 'class': 'form-control col-md-6'}),
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
                    required = True,
                    label='شماره سفارش',
                    widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'شماره سفارش'}),)

    create_Date = forms.DateField(
        required=True,
        label='تاریخ ثبت سفارش ',
        widget=DateInput(attrs={'class': 'form-control mb-3'}), )

    request_code = forms.CharField(
                    required = True,
                    label='شماره / کد درخواست کالا',
                    widget=forms.TextInput(attrs={'class': 'form-control mb-3 '}))

    # dueDate = forms.DateField(
    #                     required = True,
    #                     label='تاریخ تحویل سفارش ',
    #                     widget=DateInput(attrs={'class': 'form-control mb-3'}),)

    #     self.fields['dueDate'] = JalaliDateField(label=_('تاریخ تحویل سفارش'),
    #                                                         widget=AdminSplitJalaliDateTime
    #                                                         # required, for decompress DatetimeField to JalaliDateField and JalaliTimeField
    #                                                         )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-6'),
                Column('create_Date', css_class='form-group col-md-6'),
                css_class='form-row'),
            Row(
                Column('request_code', css_class='form-group col-md-6'),
                Column('dueDate', css_class='form-group col-md-6'),
                css_class='form-row'),


            Submit('submit', 'ثبت یا ویرایش '))

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