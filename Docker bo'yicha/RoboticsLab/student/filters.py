import django_filters
from django_filters import CharFilter, DateFilter, ChoiceFilter

from .models import Payment

class PaymentFilter(django_filters.FilterSet):
    first_name = CharFilter(field_name='student__first_name', lookup_expr='icontains')
    last_name = CharFilter(field_name='student__last_name', lookup_expr='iexact')
    middle_name = CharFilter(field_name='student__middle_name', lookup_expr='iexact')
    MONTH = [
        ('January', 'January'), ('February', 'February'),
        ('March', 'March'), ('April', 'April'),
        ('May', 'May'), ('June', 'June'),
        ('July', 'July'), ('August', 'August'),
        ('September', 'September'), ('October', 'October'),
        ('November', 'November'), ('December', 'December'),
    ]
    month = ChoiceFilter(choices=MONTH)
    start_date = DateFilter(field_name='date_paid', label='With start day', lookup_expr='gte')
    end_date = DateFilter(field_name='date_paid', label='Without end day', lookup_expr='lte')
    class Meta:
        model = Payment
        fields = '__all__'
        exclude = ['student', 'date_paid']
