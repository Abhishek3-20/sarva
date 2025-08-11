from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Note
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'notes/home.html')

@login_required
def get_notes(request):
    notes = Note.objects.filter(user=request.user).order_by('-created_at')
    return JsonResponse({
        'notes': list(notes.values('id', 'content', 'created_at'))
    })

@login_required
def save_note(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Note.objects.create(user=request.user, content=content)
    return JsonResponse({'status': 'ok'})

@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    if request.method == 'POST':
        new_content = request.POST.get('content')
        if new_content:
            note.content = new_content
            note.save()
            return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'}, status=400)

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    note.delete()
    return JsonResponse({'status': 'ok'})
