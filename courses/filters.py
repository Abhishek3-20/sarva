import django_filters
from .models import Course

class CourseFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_search')
    category = django_filters.CharFilter(field_name='category__slug')
    level = django_filters.CharFilter(field_name='level')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    tags = django_filters.CharFilter(field_name='tags__slug')
    
    class Meta:
        model = Course
        fields = ['search', 'category', 'level', 'min_price', 'max_price', 'tags']
    
    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) |
            Q(short_description__icontains=value) |
            Q(description__icontains=value) |
            Q(instructor__email__icontains=value)
        )