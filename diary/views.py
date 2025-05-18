from django.shortcuts import render, redirect, get_object_or_404
from .models import DiaryEntry
from .forms import DiaryEntryForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# def index(request):
#     entries = DiaryEntry.objects.order_by('-created_at')
#     return render(request, 'diary/index.html', {'entries': entries})
#
# def create_entry(request):
#     if request.method == 'POST':
#         form = DiaryEntryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = DiaryEntryForm()
#     return render(request, 'diary/create_entry.html', {'form': form})
#
# def delete_entry(request, entry_id):
#     entry = get_object_or_404(DiaryEntry, pk=entry_id)
#     entry.delete()
#     return redirect('index')

from django.contrib.auth.decorators import login_required

@login_required
def create_entry(request):
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('index')
    else:
        form = DiaryEntryForm()
    return render(request, 'diary/create_entry.html', {'form': form})

@login_required
def delete_entry(request, entry_id):
    entry = get_object_or_404(DiaryEntry, pk=entry_id, user=request.user)
    entry.delete()
    return redirect('index')

def index(request):
    if request.user.is_authenticated:
        entries = DiaryEntry.objects.filter(user=request.user).order_by('-created_at')
    else:
        entries = []
    return render(request, 'diary/index.html', {'entries': entries})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'diary/index.html', {'form': form})


def index(request):
    days = ["{:02d}".format(d) for d in range(1, 32)]  # '01', '02', ..., '31'

    # здесь ты, возможно, передаёшь записи дневника и другие данные
    context = {
        'days': days,
        # 'entries': entries,
        # 'query': query,
    }

    return render(request, 'diary/index.html', context)
