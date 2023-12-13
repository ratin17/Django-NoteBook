from django.shortcuts import render,redirect
from .models import Note,Entry
from .forms import Noteform

from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'notes/index.html')

@login_required
def notes(request):
    
    notes=Note.objects.order_by('-date_added')
    
    context={'notes':notes}
    
    return render(request,'notes/notes.html',context)

@login_required
def note(request,note_id):
    note=Note.objects.get(id=note_id)
    entries=note.entry_set.order_by('date_added')
    
    context={'note':note,'entries':entries}
    
    return render(request,'notes/note.html',context)
    

@login_required 
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

    