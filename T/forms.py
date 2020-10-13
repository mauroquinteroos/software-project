from django import forms
from .models import *
class Rutaform(forms.ModelForm):
    class Meta:
        model=Ruta
        vigencia =( 
        ("1", "One"), 
        ("2", "Two"), )
        zonaGPS=(
         ("1","1"),
         ("2","2")   
        ) 
        elaborado=(
        ("1","ella"),
        ("2","tu")    
        )
        fields=('__all__')
        widgets={
            'codRuta':forms.TextInput(attrs={'style':'width:40px;'}),
            'fechaRegistro':forms.TextInput(attrs={'type':'date'}),
            'vigencia':forms.Select(choices = vigencia), 
            'denominacionRuta':forms.Textarea(attrs={'rows':'4','class':'form-control'}),
            'denominacionCortoRuta':forms.TextInput(attrs={'style':'width:300px;'}),
            'nroKms':forms.TextInput(attrs={'style':'width:65px;','disabled':'true'}),
            'zonaGPS':forms.Select(choices = zonaGPS,attrs={'style':'width:80px;'}),
            'progInicio':forms.TextInput(attrs={'class':'max115'}),
            'progFinal':forms.TextInput(attrs={'class':'max115'}),
            'latitudInicioRuta':forms.TextInput(attrs={'class':'max115'}),
            'latitudFinalRuta':forms.TextInput(attrs={'class':'max115'}),
            'longitudInicioRuta':forms.TextInput(attrs={'class':'max115'}),
            'longitudFinalRuta':forms.TextInput(attrs={'class':'max115'}),
            'altitudInicioRuta':forms.TextInput(attrs={'class':'max115'}),
            'altitudFinalRuta':forms.TextInput(attrs={'class':'max115'}),
            'observacionRuta':forms.Textarea(attrs={'rows':'4','class':'form-control'}),
            'elaboradorPor':forms.Select(choices = elaborado), 
          
         # 'fechaRegistro':forms.DateField(attrs={'style':'width:100px;'})
        }

class TramoForm(forms.ModelForm):
    class Meta:
        model=Tramo
        vigencia =( 
        ("1", "uno"), 
        ("2", "dos"), )
        zonaGPS=(
         ("1","1"),
         ("2","2")   
        ) 
        fields=('__all__')
        widgets={
            'codTramo':forms.TextInput(attrs={'style':'width:40px;'}),
            'fechaRegistro':forms.TextInput(attrs={'type':'date'}),
            'vigencia':forms.Select(choices = vigencia), 
            'denominacionTramo':forms.Textarea(attrs={'rows':'4','class':'form-control'}),
            'denominacionCortoTramo':forms.TextInput(attrs={'style':'width:300px;'}),
            'zonaGPS':forms.Select(choices = zonaGPS,attrs={'style':'width:80px;'}),
            'nroKmsTramo':forms.TextInput(attrs={'style':'width:65px;'}),
            'progInicio':forms.TextInput(attrs={'class':'max115'}),
            'progFin':forms.TextInput(attrs={'class':'max115'}),
            'latitudInicioTramo':forms.TextInput(attrs={'class':'max115'}),
            'latitudFinalTramo':forms.TextInput(attrs={'class':'max115'}),
            'longitudInicioTramo':forms.TextInput(attrs={'class':'max115'}),
            'longitudFinalTramo':forms.TextInput(attrs={'class':'max115'}),
            'altitudInicioTramo':forms.TextInput(attrs={'class':'max115'}),
            'altitudFinalTramo':forms.TextInput(attrs={'class':'max115'}),
            'observacionTramo':forms.Textarea(attrs={'rows':'4','class':'form-control'}),
        }
    
  
