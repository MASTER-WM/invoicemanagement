import django_filters
from django_filters import DateFilter
from .models import *

class InvoiceFilter(django_filters.FilterSet):

    CHOICES = (
        ('Accen', 'صعودی'),
        ('Deccen', 'نزولی')

        )

    title_filter = django_filters.CharFilter(label = 'شماره سفارش:', field_name='title', lookup_expr = 'icontains')
    client__clientName = django_filters.CharFilter(label = 'نام مشتری:', lookup_expr = 'icontains')
    # create_Date_gt = DateFilter(label = 'سفارشات بعد از تاریخ:', field_name='create_Date', lookup_expr='gte')
    # create_Date_lt = DateFilter(label = 'سفارشات قبل از تاریخ:', field_name='create_Date', lookup_expr='lte')
    request_code_filter = django_filters.CharFilter(label = 'شماره درخواست:', field_name = 'request_code', lookup_expr = 'icontains')
    ordering = django_filters.ChoiceFilter(label='مرتب سازی زمانی', choices = CHOICES, method='filter_by_order')
    invoiceRelated__title = django_filters.CharFilter(label = 'نام محصول:', lookup_expr = 'icontains')
    invoiceRelated__description = django_filters.CharFilter(label='توضیحات محصول:', lookup_expr='icontains')


    def filter_by_order(self,queryset, name, value):
        expression = 'create_Date' if value == 'Accen' else '-create_Date'
        return queryset.order_by(expression)

class ClientFilter(django_filters.FilterSet):
    clientName = django_filters.CharFilter(label='نام مشتری:',field_name='clientName', lookup_expr='icontains')