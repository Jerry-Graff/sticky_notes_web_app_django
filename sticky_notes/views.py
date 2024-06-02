from django.shortcuts import render, get_object_or_404, redirect
from .models import StickyNotes
from .forms import StickyNotesForm


def sticky_note_list(request):
    '''
    Function to display list of sticky notes
    '''
    notes = StickyNotes.objects.all()
    return render(request, "sticky_notes/note_list.html", {"notes": notes})


def sticky_note_detail(request, pk):
    '''
    Function to display sticky note details
    '''
    note = get_object_or_404(StickyNotes, pk=pk)
    return render(request, "sticky_notes/note_detail.html", {"note": note})


def sticky_note_create(request):
    '''
    Function to create new sticky note
    '''
    if request.method == 'POST':
        form = StickyNotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = StickyNotesForm()
    return render(request, 'sticky_notes/note_form.html', {'form': form})


def sticky_note_update(request, pk):
    '''
    Function to update a created sticky note
    '''
    note = get_object_or_404(StickyNotes, pk=pk)
    if request.method == "POST":
        form = StickyNotesForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = StickyNotesForm(instance=note)
    return render(request, 'sticky_notes/note_form.html', {'form': form})


def sticky_note_delete(request, pk):
    '''
    Function to delete a sticky note
    '''
    note = get_object_or_404(StickyNotes, pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect('note_list')
    return render(
        request, 'sticky_notes/note_confirm_delete.html', {'note': note})


def add_line_breaks(content, interval=15):
    """
    Utility function to add line breaks on individual sticky notes.
    """
    return '\n'.join(
        [content[i:i+interval] for i in range(0, len(content), interval)])
