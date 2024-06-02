from django import forms
from .models import StickyNotes


class StickyNotesForm(forms.ModelForm):

    class Meta:
        model = StickyNotes
        fields = ["title", "content"]
