from django import forms


class Autosform(forms.Form):
    marca=forms.CharField(max_length=50)
    modelo=forms.CharField(max_length=50)

class Camionetasform(forms.Form):
    marca=forms.CharField(max_length=50)
    modelo=forms.CharField(max_length=50)


class Motosform(forms.Form):
    marca=forms.CharField(max_length=50)
    modelo=forms.CharField(max_length=50)