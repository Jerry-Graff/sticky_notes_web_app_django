from django.test import TestCase
from django.urls import reverse
from .models import StickyNotes


class StickyNotesModelTests(TestCase):

    def setUp(self):
        self.note = StickyNotes.objects.create(
            title="Test Sticky Note",
            content="This is a test note"
        )

    def test_note_has_title(self):
        post = StickyNotes.objects.get(id=1)
        self.assertEqual(post.title, "Test Sticky Note")

    def test_note_has_content(self):
        post = StickyNotes.objects.get(id=1)
        self.assertEqual(post.content, "This is a test note")

    def test_note_str(self):
        self.assertEqual(str(self.note), "Test Sticky Note")


class StickyNotesViewsTests(TestCase):

    def setUp(self):
        self.note = StickyNotes.objects.create(
            title="Test Sticky Note",
            content="This is a test note"
        )

    def test_note_list_view(self):
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Sticky Note")
        self.assertTemplateUsed(response, "sticky_notes/note_list.html")

    def test_note_detail_view(self):
        response = self.client.get(reverse("note_detail", args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Sticky Note")
        self.assertTemplateUsed(response, "sticky_notes/note_detail.html")
