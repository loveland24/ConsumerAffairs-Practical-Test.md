from django_filters import rest_framework as filters
from event.models import Event


class EventFilter(filters.FilterSet):
    session = filters.CharFilter(method='session_filter')
    timestamp_gte = filters.DateTimeFilter(field_name="timestamp", lookup_expr='gte')
    timestamp_lte = filters.DateTimeFilter(field_name="timestamp", lookup_expr='lte')

    class Meta:
        model = Event
        fields = '__all__'

    def session_filter(self, queryset, name, value):
        return queryset.filter(session_id=value).distinct()