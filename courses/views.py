from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q, Avg
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from .models import Course, CourseCategory, Enrollment, Review
from .filters import CourseFilter

class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'
    paginate_by = 9
    
    def get_queryset(self):
        queryset = Course.objects.filter(is_active=True).select_related('instructor', 'category').prefetch_related('tags')
        
        # Filtering
        self.filterset = CourseFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs.annotate(
            avg_rating=Avg('reviews__rating')
        ).order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CourseCategory.objects.all()
        context['filterset'] = self.filterset
        return context

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.object
        
        # Check if user is enrolled
        is_enrolled = False
        if self.request.user.is_authenticated:
            is_enrolled = Enrollment.objects.filter(
                student=self.request.user,
                course=course
            ).exists()
        
        # Get average rating
        avg_rating = Review.objects.filter(course=course).aggregate(Avg('rating'))['rating__avg']
        
        context.update({
            'is_enrolled': is_enrolled,
            'avg_rating': avg_rating,
            'reviews': Review.objects.filter(course=course).select_related('user'),
            'modules': course.modules.all().prefetch_related('lessons'),
        })
        return context