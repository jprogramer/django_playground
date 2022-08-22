from django.shortcuts import render
from django.db import models

# Create your models here.

class Actif(models.Model):
    id = models.IntegerField(primary_key=True)
    nom=models.CharField(max_length=50,null=True)
    classement = models.CharField(max_length=100,null=True)
    description = models.TextField(max_length=255,null=True)
    retenu = models.CharField(max_length=20,null=True)
    valeur =models.IntegerField(null=True)
    
class Vul(models.Model):
    id = models.IntegerField(primary_key=True)
    nom=models.CharField(max_length=50,null=True)
    
acts={
    Actif(id=1,nom='act1_nom',classement='act1_classement',description='act1_desc',retenu='act1_retenu',valeur=101),
    Actif(id=2,nom='act2_nom',classement='act2_classement',description='act2_desc',retenu='act2_retenu',valeur=102),
    Actif(id=3,nom='act3_nom',classement='act3_classement',description='act3_desc',retenu='act3_retenu',valeur=103),
}

vuls={
    Vul(id=1,nom='vul1_nom'),
    Vul(id=2,nom='vul2_nom'),
    Vul(id=3,nom='vul3_nom'),
}

def analyse(request):
    context={
        'act' : acts,
        'vul': vuls,
    }
    return render(request, 'risqueAna.html',context)

def add_object(request, vul):
    return render(request, 'addObject.html', {'vul': vul})

def about(request):
    return render(request, 'about.html', {'name': 'joseph'})