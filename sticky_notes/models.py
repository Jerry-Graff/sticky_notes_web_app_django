from django.db import models


class StickyNotes(models.Model):  # Class to display sticky note
    title = models.CharField(max_length=22)  # Max len for error handling
    content = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):  # Str method for display purposes
        return self.title

    def getsummery(self):
        return self.content[:75]

    class Meta:  # Using Djangos inbuilt function for timestamp
        ordering = ["-created_at"]
