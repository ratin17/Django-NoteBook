from django.shortcuts import render,redirect
from .models import Note,Entry
from .forms import Noteform

MyNotes=[{'id':1,'title':'First Note','entries':['Entry 1.1','Entry 1.2','Entry 1.3']},
         {'id':2,'title':'Second Note','entries':['Entry 2.1','Entry 2.2','Entry 2.3']},
         {'id':3,'title':'Third Note','entries':['Entry 3.1','Entry 3.2','Entry 3.3']},
         ]

def index(request):
    return render(request,'notes/index.html')


def notes(request):
    
    notes=Note.objects.order_by('-date_added')
    
    context={'notes':notes}
    
    return render(request,'notes/notes.html',context)

def note(request,note_id):
    note=Note.objects.get(id=note_id)
    entries=note.entry_set.order_by('date_added')
    
    context={'note':note,'entries':entries}
    
    return render(request,'notes/note.html',context)
    
    
def new_note(request):
    if request.method !='POST':
        form=Noteform()
    else:
        form=Noteform(data=request.POST)
        if form.is_valid():
            new_note=form.save()
            new_note.save()
            return redirect('notes:notes')
    context={'form':form}
    return render(request,'notes/new_note.html',context)

    