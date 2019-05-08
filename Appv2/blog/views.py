from django.shortcuts import render, redirect, HttpResponse
from .models import Responsable , Clinique , Sanatorium , Hote
from django.contrib.auth import authenticate
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
@login_required
def home(request):
    context = {
        'responsables': Responsable.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request): 
    return render(request, 'blog/about.html')

def login(request):
    return render(request, 'blog/login.html')


def create(request):
    print(request.POST)
    name = request.GET['name']
    prenom = request.GET['prenom']
    email = request.GET['email']
    password = request.GET['password']
    adresse = request.GET['adresse']

    responsable_details = Responsable(name=name, prenom=prenom, email=email, password=password, adresse=adresse)
    responsable_details.save()
    return redirect('/')


def add_responsable(request):
    return render(request, 'blog/add_responsable.html')



def delete(request, id):
    reponsables = Responsable.objects.get(id_responsable=id)
    reponsables.delete()
    return redirect('/')

def edit(request, id):
    reponsables = Responsable.objects.get(id_responsable=id)
    context = {
        'reponsables': reponsables
    }
    return render(request, 'blog/edit.html', context)


def update(request, id):
    reponsables = Responsable.objects.get(id_responsable=id)
    reponsables.name = request.GET['name']
    reponsables.prenom = request.GET['prenom']
    reponsables.email = request.GET['email']
    reponsables.password = request.GET['password']
    reponsables.adresse = request.GET['adresse']

    reponsables.save()
    return redirect('/')

def loginresp(request):
    context = {}
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        responsable = authenticate(request, email=email, password=password)
        if responsable:
                    return redirect('/')
            

    else:
        return render(request, 'blog/login.html', context)

def clinique(request): 
  context = {
        'cliniques': Clinique.objects.all()
    }
    
  return render(request, 'blog/hospital.html', context)

def add_clinique(request):
    return render(request, 'blog/add_clinique.html')

def create_clinique(request):

    print(request.POST)
    name = request.GET['name']
    description = request.GET['description']
    adresse = request.GET['adresse']

    clinique_details = Clinique(name=name, description=description, adresse=adresse , Image="")
    clinique_details.save()
    return redirect('/clinique')

def delete_clinique(request, id):
    reponsables = Clinique.objects.get(id_clinique=id)
    reponsables.delete()
    return redirect('/clinique')

def edit_clinique(request, id):
    cliniques = Clinique.objects.get(id_clinique=id)
    context = {
        'cliniques': cliniques
    }
    return render(request, 'blog/edit_clinique.html', context)


def update_clinique(request, id):
    cliniques = Clinique.objects.get(id_clinique=id)
    cliniques.name = request.GET['name']
    cliniques.description = request.GET['description']
    cliniques.adresse = request.GET['adresse']
    cliniques.Image = ""

    cliniques.save()
    return redirect('/clinique')



def sanatorium(request): 
  context = {
        'sanatoriums': Sanatorium.objects.all()
    }
    
  return render(request, 'blog/sanatorium.html', context)

def add_sanatorium(request):
    return render(request, 'blog/add_sanatorium.html')

def create_sanatorium(request):

    print(request.POST)
    name = request.GET['name']
    description = request.GET['description']
    adresse = request.GET['adresse']
    telephone = request.GET['telephone']
    sanatorium_details = Sanatorium(name=name, description=description, adresse=adresse ,telephone=telephone, Image="")
    sanatorium_details.save()
    return redirect('/sanatorium')

def delete_sanatorium(request, id):
    sanatoriums = Sanatorium.objects.get(id_sanatorium=id)
    sanatoriums.delete()
    return redirect('/sanatorium')

def edit_sanatorium(request, id):
    sanatoriums = Sanatorium.objects.get(id_sanatorium=id)
    context = {
        'sanatoriums': sanatoriums
    }
    return render(request, 'blog/edit_sanatorium.html', context)


def update_sanatorium(request, id):
    sanatoriums = Sanatorium.objects.get(id_sanatorium=id)
    sanatoriums.name = request.GET['name']
    sanatoriums.description = request.GET['description']
    sanatoriums.adresse = request.GET['adresse']
    sanatoriums.telephone = request.GET['telephone']
    sanatoriums.Image = ""

    sanatoriums.save()
    return redirect('/sanatorium')



def hote(request): 
  context = {
        'hotes': Hote.objects.all()
    }
    
  return render(request, 'blog/hote.html', context)

def add_hote(request):
    return render(request, 'blog/add_hote.html')

def create_hote(request):

    print(request.POST)
    name = request.GET['name']
    description = request.GET['description']
    adresse = request.GET['adresse']
    telephone = request.GET['telephone']
    hote_details = Hote(name=name, description=description, adresse=adresse ,telephone=telephone, Image="")
    hote_details.save()
    return redirect('/hote')

def delete_hote(request, id):
    hotes = Hote.objects.get(id_hote=id)
    hotes.delete()
    return redirect('/hote')

def edit_hote(request, id):
    hotes = Hote.objects.get(id_hote=id)
    context = {
        'hotes': hotes
    }
    return render(request, 'blog/edit_hote.html', context)


def update_hote(request, id):
    hotes = Hote.objects.get(id_hote=id)
    hotes.name = request.GET['name']
    hotes.description = request.GET['description']
    hotes.adresse = request.GET['adresse']
    hotes.telephone = request.GET['telephone']
    hotes.Image = ""

    hotes.save()
    return redirect('/hote')