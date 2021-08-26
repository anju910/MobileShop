import django_filters
from owner.models import Mobile
class MobileFilter(django_filters.FilterSet):
    mobile_name=django_filters.CharFilter(field_name="mobile_name",lookup_expr="contains")
    price_lt=django_filters.NumberFilter(field_name="price",lookup_expr="lt")
    price_gt=django_filters.NumberFilter(field_name="price",lookup_expr="gt")

    class Meta:
        model=Mobile
        fields=["brand","os"]