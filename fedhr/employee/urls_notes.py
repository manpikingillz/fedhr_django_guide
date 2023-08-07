from django.urls import path

from fedhr.employee.api.note import (
    NoteCreateApi,
    NoteListApi,
    NoteDetailApi,
    NoteUpdateApi,
    NoteDeleteApi,
)

urlpatterns = [
    path('create/', NoteCreateApi.as_view(), name='note_create'),
    path('', NoteListApi.as_view(), name='note_list'),
    path('<int:note_id>/', NoteDetailApi.as_view(), name='note_detail'),
    path('<int:note_id>/update/', NoteUpdateApi.as_view(), name='note_update'),
    path('<int:note_id>/delete/', NoteDeleteApi.as_view(), name='note_delete'),
]