from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='notes-home'),
    path('get/', views.get_notes, name='get_notes'),
    path('save/', views.save_note, name='save_note'),
    path('edit/<int:note_id>/', views.edit_note, name='edit_note'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
]
