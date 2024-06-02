from django.urls import path
from . import views

# url paths for CRUD functionality
urlpatterns = [
    path('', views.sticky_note_list, name='note_list'),
    path('note/<int:pk>/',
         views.sticky_note_detail, name='note_detail'),
    path('note/new/',
         views.sticky_note_create, name='note_create'),
    path('note/<int:pk>/edit/',
         views.sticky_note_update, name='note_update'),
    path(
        'note/<int:pk>/delete/',
        views.sticky_note_delete, name='note_delete'),
]
