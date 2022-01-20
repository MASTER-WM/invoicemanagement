import django_filters
from .models import *

class ProductFilter(django_filters.FilterSet):
    price_filter = django_filters.NumberFilter(field_name='price', lookup_expr='gte')

class InvoiceFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title')
    create_Date = django_filters.NumberFilter(field_name='create_Date', lookup_expr='gte')
