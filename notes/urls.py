from django.urls import path

from . import views

app_name="notes"
urlpatterns = [
    path('home/',views.index,name='index'),
    path('notes/',views.notes,name='notes'),
    path('note/<int:note_id>',views.note,name='note'),
    path('new_note/',views.new_note,name='new_note'),
    
    
]