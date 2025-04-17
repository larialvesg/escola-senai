from django import forms

class ExcelUploadForm(forms.Form):
    file = forms.FileField(label="Selecione um arquivo CSV")

class ExcelUploadTemp(forms.Form):
    file = forms.FileField(label="Selecione um arquivo CSV de Temperatura")

class ExcelUploadCont(forms.Form):
    file = forms.FileField(label="Selecione um arquivo CSV de Contador")

class ExcelUploadUmi(forms.Form):
    file = forms.FileField(label="Selecione um arquivo CSV de Umidade")

class ExcelUploadLumi(forms.Form):
    file = forms.FileField(label="Selecione um arquivo CSV de Luminosidade")


    